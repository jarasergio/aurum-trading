from datetime import UTC, datetime, timedelta
from decimal import Decimal
from uuid import uuid4

import pytest

from app.models.instrument import Instrument
from app.models.market_tick import MarketTick
from app.schemas.market_data import MarketQuoteCreate
from app.services.market_data_service import (
    delete_expired_ticks,
    get_market_ticks,
    save_market_quote,
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
        datetime.now(UTC),
        Decimal(65000),
    )

    result = save_market_quote(db_session, quote)

    assert result.instrument_id == instrument.id
    assert result.last == Decimal(65000)

    ticks = get_market_ticks(db_session, instrument.id)

    assert len(ticks) == 1
    assert ticks[0].last == Decimal(65000)


def test_newer_quote_updates_current_quote(db_session):
    instrument = create_instrument(db_session)

    now = datetime.now(UTC)

    first = create_quote(
        instrument.id,
        now,
        Decimal(65000),
    )

    second = create_quote(
        instrument.id,
        now + timedelta(minutes=1),
        Decimal(66000),
    )

    save_market_quote(db_session, first)
    result = save_market_quote(db_session, second)

    assert result.last == Decimal(66000)

    ticks = get_market_ticks(db_session, instrument.id)

    assert len(ticks) == 2


def test_older_quote_does_not_replace_current_quote(db_session):
    instrument = create_instrument(db_session)

    now = datetime.now(UTC)

    newer = create_quote(
        instrument.id,
        now,
        Decimal(66000),
    )

    older = create_quote(
        instrument.id,
        now - timedelta(minutes=5),
        Decimal(65000),
    )

    save_market_quote(db_session, newer)
    result = save_market_quote(db_session, older)

    assert result.last == Decimal(66000)

    ticks = get_market_ticks(db_session, instrument.id)

    assert len(ticks) == 2


def test_delete_expired_ticks(db_session):
    instrument = create_instrument(db_session)

    now = datetime.now(UTC)

    quote = create_quote(
        instrument.id,
        now,
        Decimal(65000),
    )

    save_market_quote(db_session, quote)
    save_market_quote(
        db_session,
        create_quote(
            instrument.id,
            now + timedelta(seconds=1),
            Decimal(65100),
        ),
    )

    # Simulamos ticks recibidos hace ocho días.
    expired_date = now - timedelta(days=8)

    db_session.query(MarketTick).update({MarketTick.received_at: expired_date})
    db_session.commit()

    # Insertamos un tick reciente.
    save_market_quote(
        db_session,
        create_quote(
            instrument.id,
            now + timedelta(seconds=2),
            Decimal(65200),
        ),
    )

    deleted = delete_expired_ticks(db_session)

    assert deleted == 2

    remaining = get_market_ticks(db_session, instrument.id)

    assert len(remaining) == 1
    assert remaining[0].last == Decimal(65200)


def test_get_market_ticks_filters_by_provider(db_session):
    instrument = create_instrument(db_session)
    now = datetime.now(UTC)

    save_market_quote(
        db_session,
        create_quote(
            instrument.id,
            now,
            Decimal(65000),
        ),
    )

    other_provider_quote = create_quote(
        instrument.id,
        now + timedelta(minutes=1),
        Decimal(66000),
    )
    other_provider_quote.provider = "another_provider"

    save_market_quote(db_session, other_provider_quote)

    ticks = get_market_ticks(
        db_session,
        instrument.id,
        provider="test_provider",
    )

    assert len(ticks) == 1
    assert ticks[0].provider == "test_provider"


def test_get_market_ticks_filters_by_start_time(db_session):
    instrument = create_instrument(db_session)
    now = datetime.now(UTC)

    for minutes, price in [
        (0, "65000"),
        (5, "65100"),
        (10, "65200"),
    ]:
        save_market_quote(
            db_session,
            create_quote(
                instrument.id,
                now + timedelta(minutes=minutes),
                Decimal(price),
            ),
        )

    ticks = get_market_ticks(
        db_session,
        instrument.id,
        start_time=now + timedelta(minutes=5),
    )

    assert len(ticks) == 2
    assert all(tick.market_timestamp >= now + timedelta(minutes=5) for tick in ticks)


def test_get_market_ticks_filters_by_end_time(db_session):
    instrument = create_instrument(db_session)
    now = datetime.now(UTC)

    for minutes, price in [
        (0, "65000"),
        (5, "65100"),
        (10, "65200"),
    ]:
        save_market_quote(
            db_session,
            create_quote(
                instrument.id,
                now + timedelta(minutes=minutes),
                Decimal(price),
            ),
        )

    ticks = get_market_ticks(
        db_session,
        instrument.id,
        end_time=now + timedelta(minutes=5),
    )

    assert len(ticks) == 2
    assert all(tick.market_timestamp <= now + timedelta(minutes=5) for tick in ticks)


def test_get_market_ticks_filters_by_time_range(db_session):
    instrument = create_instrument(db_session)
    now = datetime.now(UTC)

    for minutes, price in [
        (0, "65000"),
        (5, "65100"),
        (10, "65200"),
        (15, "65300"),
    ]:
        save_market_quote(
            db_session,
            create_quote(
                instrument.id,
                now + timedelta(minutes=minutes),
                Decimal(price),
            ),
        )

    ticks = get_market_ticks(
        db_session,
        instrument.id,
        start_time=now + timedelta(minutes=5),
        end_time=now + timedelta(minutes=10),
    )

    assert len(ticks) == 2


def test_get_market_ticks_rejects_naive_start_time(db_session):
    instrument = create_instrument(db_session)

    naive_datetime = datetime(2026, 1, 1, 12, 0, 0)

    with pytest.raises(ValueError, match="start_time must include timezone"):
        get_market_ticks(
            db_session,
            instrument.id,
            start_time=naive_datetime,
        )


def test_get_market_ticks_rejects_invalid_time_range(db_session):
    instrument = create_instrument(db_session)

    start = datetime(2026, 1, 2, tzinfo=UTC)
    end = datetime(2026, 1, 1, tzinfo=UTC)

    with pytest.raises(
        ValueError,
        match="start_time cannot be after end_time",
    ):
        get_market_ticks(
            db_session,
            instrument.id,
            start_time=start,
            end_time=end,
        )


def test_get_market_ticks_rejects_invalid_limit(db_session):
    instrument = create_instrument(db_session)

    with pytest.raises(
        ValueError,
        match="Limit must be between 1 and 5000",
    ):
        get_market_ticks(
            db_session,
            instrument.id,
            limit=0,
        )
