
from datetime import datetime, timedelta, timezone

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models.instrument import Instrument
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
) -> list[MarketTick]:
    """
    Devuelve los ticks más recientes de un instrumento.
    """

    if not 1 <= limit <= 5000:
        raise ValueError("Limit must be between 1 and 5000")

    statement = (
        select(MarketTick)
        .where(MarketTick.instrument_id == instrument_id)
        .order_by(
            MarketTick.market_timestamp.desc(),
            MarketTick.id.desc(),
        )
        .limit(limit)
    )

    return list(db.scalars(statement).all())


def delete_expired_ticks(db: Session) -> int:
    """
    Elimina ticks recibidos hace más de siete días.
    """

    cutoff = datetime.now(timezone.utc) - timedelta(
        days=TICK_RETENTION_DAYS
    )

    statement = delete(MarketTick).where(
        MarketTick.received_at < cutoff
    )

    try:
        result = db.execute(statement)
        deleted_count = result.rowcount or 0

        db.commit()

        return deleted_count

    except Exception:
        db.rollback()
        raise
