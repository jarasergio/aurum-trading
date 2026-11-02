from datetime import UTC, datetime, timedelta

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models.instrument import Instrument
from app.models.market_candle import MarketCandle
from app.models.market_quote import MarketQuote
from app.models.market_tick import MarketTick
from app.schemas.market_data import MarketQuoteCreate

TICK_RETENTION_DAYS = 7


def save_market_quote(
    db: Session,
    quote_data: MarketQuoteCreate,
) -> MarketQuote:
    """
    Guarda un tick y actualiza la última cotización
    si el dato recibido es más reciente.
    """

    instrument = db.get(Instrument, quote_data.instrument_id)

    if instrument is None:
        raise ValueError("Instrument not found")

    quote_values = quote_data.model_dump()

    try:
        statement = select(MarketQuote).where(
            MarketQuote.instrument_id == quote_data.instrument_id,
            MarketQuote.provider == quote_data.provider,
        )

        current_quote = db.scalar(statement)

        if current_quote is None:
            current_quote = MarketQuote(**quote_values)
            db.add(current_quote)

        elif quote_data.market_timestamp >= current_quote.market_timestamp:
            current_quote.bid = quote_data.bid
            current_quote.ask = quote_data.ask
            current_quote.last = quote_data.last
            current_quote.market_timestamp = quote_data.market_timestamp

        tick = MarketTick(**quote_values)
        db.add(tick)

        db.commit()
        db.refresh(current_quote)

        return current_quote

    except Exception:
        db.rollback()
        raise


def get_latest_quotes(
    db: Session,
    instrument_id: int,
) -> list[MarketQuote]:
    """
    Devuelve las últimas cotizaciones de un instrumento,
    ordenadas por proveedor.
    """

    statement = (
        select(MarketQuote)
        .where(MarketQuote.instrument_id == instrument_id)
        .order_by(MarketQuote.provider)
    )

    return list(db.scalars(statement).all())


def get_market_ticks(
    db: Session,
    instrument_id: int,
    limit: int = 500,
    provider: str | None = None,
    start_time: datetime | None = None,
    end_time: datetime | None = None,
) -> list[MarketTick]:
    """
    Devuelve ticks de un instrumento con filtros opcionales.

    Los ticks se conservan durante siete días.
    El límite controla el número máximo de resultados,
    no el período histórico.
    """

    if not 1 <= limit <= 5000:
        raise ValueError("Limit must be between 1 and 5000")

    if start_time is not None and start_time.utcoffset() is None:
        raise ValueError("start_time must include timezone")

    if end_time is not None and end_time.utcoffset() is None:
        raise ValueError("end_time must include timezone")

    if start_time is not None and end_time is not None and start_time > end_time:
        raise ValueError("start_time cannot be after end_time")

    statement = select(MarketTick).where(MarketTick.instrument_id == instrument_id)

    if provider is not None:
        statement = statement.where(MarketTick.provider == provider)

    if start_time is not None:
        statement = statement.where(MarketTick.market_timestamp >= start_time)

    if end_time is not None:
        statement = statement.where(MarketTick.market_timestamp <= end_time)

    statement = statement.order_by(
        MarketTick.market_timestamp.desc(),
        MarketTick.id.desc(),
    ).limit(limit)

    return list(db.scalars(statement).all())


def get_market_candles(
    db: Session,
    instrument_id: int,
    timeframe: str,
    start_time: datetime | None = None,
    end_time: datetime | None = None,
    limit: int = 1000,
) -> list[MarketCandle]:
    """
    Devuelve velas históricas de un instrumento,
    filtradas por timeframe y rango temporal.
    """

    if not 1 <= limit <= 10000:
        raise ValueError("Limit must be between 1 and 10000")

    if start_time is not None and start_time.utcoffset() is None:
        raise ValueError("start_time must include timezone")

    if end_time is not None and end_time.utcoffset() is None:
        raise ValueError("end_time must include timezone")

    if start_time is not None and end_time is not None and start_time > end_time:
        raise ValueError("start_time cannot be after end_time")

    statement = select(MarketCandle).where(
        MarketCandle.instrument_id == instrument_id,
        MarketCandle.timeframe == timeframe,
    )

    if start_time is not None:
        statement = statement.where(MarketCandle.open_time >= start_time)

    if end_time is not None:
        statement = statement.where(MarketCandle.open_time <= end_time)

    statement = statement.order_by(
        MarketCandle.open_time.desc(),
        MarketCandle.id.desc(),
    ).limit(limit)

    return list(db.scalars(statement).all())


def delete_expired_ticks(db: Session) -> int:
    """
    Elimina ticks recibidos hace más de siete días.
    """

    cutoff = datetime.now(UTC) - timedelta(days=TICK_RETENTION_DAYS)

    statement = delete(MarketTick).where(MarketTick.received_at < cutoff)

    try:
        result = db.execute(statement)
        deleted_count = result.rowcount or 0

        db.commit()

        return deleted_count

    except Exception:
        db.rollback()
        raise
