
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from uuid import uuid4

from app.models.instrument import Instrument
from app.models.market_tick import MarketTick
from app.schemas.market_data import MarketQuoteCreate
from app.services.market_data_service import (
    save_market_quote,
    get_latest_quotes,
    get_market_ticks,
    delete_expired_ticks,
)


def create_instrument(db_session):
    instrument = Instrument(
        symbol=f"TEST-{uuid4().hex[:8].upper()}",
        name="Test Instrument",
        asset_class="crypto",
        market="test",
    )

    db_session.add(instrument)
    db_session.flush()

    return instrument


def create_quote(instrument_id, timestamp, last):
    return MarketQuoteCreate(
        instrument_id=instrument_id,
        provider="test_provider",
        bid=Decimal(str(last - Decimal("0.01"))),
        ask=Decimal(str(last + Decimal("0.01"))),
        last=last,
        market_timestamp=timestamp,
    )


def test_save_market_quote(db_session):
    instrument = create_instrument(db_session)

    quote = create_quote(
        instrument.id,
        datetime.now(timezone.utc),
        Decimal("65000"),
    )

    result = save_market_quote(db_session, quote)

    assert result.instrument_id == instrument.id
    assert result.last == Decimal("65000")

    ticks = get_market_ticks(db_session, instrument.id)

    assert len(ticks) == 1
    assert ticks[0].last == Decimal("65000")


def test_newer_quote_updates_current_quote(db_session):
    instrument = create_instrument(db_session)

    now = datetime.now(timezone.utc)

    first = create_quote(
        instrument.id,
        now,
        Decimal("65000"),
    )

    second = create_quote(
        instrument.id,
        now + timedelta(minutes=1),
        Decimal("66000"),
    )

    save_market_quote(db_session, first)
    result = save_market_quote(db_session, second)

    assert result.last == Decimal("66000")

    ticks = get_market_ticks(db_session, instrument.id)

    assert len(ticks) == 2


def test_older_quote_does_not_replace_current_quote(db_session):
    instrument = create_instrument(db_session)

    now = datetime.now(timezone.utc)

    newer = create_quote(
        instrument.id,
        now,
        Decimal("66000"),
    )

    older = create_quote(
        instrument.id,
        now - timedelta(minutes=5),
        Decimal("65000"),
    )

    save_market_quote(db_session, newer)
    result = save_market_quote(db_session, older)

    assert result.last == Decimal("66000")

    ticks = get_market_ticks(db_session, instrument.id)

    assert len(ticks) == 2


def test_delete_expired_ticks(db_session):
    instrument = create_instrument(db_session)

    now = datetime.now(timezone.utc)

    quote = create_quote(
        instrument.id,
        now,
        Decimal("65000"),
    )

    save_market_quote(db_session, quote)
    save_market_quote(
        db_session,
        create_quote(
            instrument.id,
            now + timedelta(seconds=1),
            Decimal("65100"),
        ),
    )

    # Simulamos ticks recibidos hace ocho días.
    expired_date = now - timedelta(days=8)

    db_session.query(MarketTick).update(
        {MarketTick.received_at: expired_date}
    )
    db_session.commit()

    # Insertamos un tick reciente.
    save_market_quote(
        db_session,
        create_quote(
            instrument.id,
            now + timedelta(seconds=2),
            Decimal("65200"),
        ),
    )

    deleted = delete_expired_ticks(db_session)

    assert deleted == 2

    remaining = get_market_ticks(db_session, instrument.id)

    assert len(remaining) == 1
    assert remaining[0].last == Decimal("65200")
