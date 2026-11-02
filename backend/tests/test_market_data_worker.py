from datetime import UTC, datetime
from decimal import Decimal
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.providers.base import NormalizedQuote
from app.workers.market_data_worker import MarketDataWorker, WorkerResult


@pytest.fixture
def mock_db():
    return MagicMock()


@pytest.fixture
def mock_provider():
    provider = MagicMock()
    provider.name = "binance"
    provider.fetch_quote = AsyncMock(
        return_value=NormalizedQuote(
            symbol="BTCUSDT",
            provider="binance",
            bid=Decimal("65000"),
            ask=Decimal("65100"),
            last=Decimal("65050"),
            timestamp=datetime.now(UTC),
        )
    )
    return provider


@pytest.fixture
def mock_registry(mock_provider):
    registry = MagicMock()
    registry.list_providers.return_value = ["binance"]
    registry.get.return_value = mock_provider
    return registry


@pytest.fixture
def mock_instrument():
    instrument = MagicMock()
    instrument.id = 1
    instrument.symbol = "BTCUSDT"
    return instrument


@pytest.fixture
def worker(mock_db, mock_registry):
    return MarketDataWorker(
        session_factory=lambda: mock_db,
        registry=mock_registry,
    )


@pytest.mark.anyio
async def test_worker_processes_active_instruments(
    worker,
    mock_db,
    mock_registry,
    mock_instrument,
):
    with (
        patch(
            "app.workers.market_data_worker.instrument_service.get_instruments",
            return_value=[mock_instrument],
        ),
        patch(
            "app.workers.market_data_worker.market_data_service.save_market_quote"
        ) as save_quote,
    ):
        result = await worker.run_once()

    assert isinstance(result, WorkerResult)
    assert result.instruments_processed == 1
    assert result.quotes_saved == 1
    assert result.quotes_failed == 0
    assert result.errors == ()

    save_quote.assert_called_once()
    mock_registry.get.assert_called_once_with("binance")
    mock_db.close.assert_called_once()


@pytest.mark.anyio
async def test_worker_continues_when_provider_fails(
    worker,
    mock_db,
    mock_registry,
    mock_provider,
    mock_instrument,
):
    mock_provider.fetch_quote.side_effect = RuntimeError("Provider unavailable")

    with (
        patch(
            "app.workers.market_data_worker.instrument_service.get_instruments",
            return_value=[mock_instrument],
        ),
        patch(
            "app.workers.market_data_worker.market_data_service.save_market_quote"
        ) as save_quote,
    ):
        result = await worker.run_once()

    assert result.instruments_processed == 1
    assert result.quotes_saved == 0
    assert result.quotes_failed == 1
    assert len(result.errors) == 1

    save_quote.assert_not_called()
    mock_db.close.assert_called_once()


@pytest.mark.anyio
async def test_worker_continues_with_other_instruments(
    worker,
    mock_db,
    mock_provider,
):
    first_instrument = MagicMock(id=1, symbol="BTCUSDT")
    second_instrument = MagicMock(id=2, symbol="ETHUSDT")

    mock_provider.fetch_quote.side_effect = [
        RuntimeError("BTC unavailable"),
        NormalizedQuote(
            symbol="ETHUSDT",
            provider="binance",
            bid=Decimal("3000"),
            ask=Decimal("3010"),
            last=Decimal("3005"),
            timestamp=datetime.now(UTC),
        ),
    ]

    with (
        patch(
            "app.workers.market_data_worker.instrument_service.get_instruments",
            return_value=[first_instrument, second_instrument],
        ),
        patch(
            "app.workers.market_data_worker.market_data_service.save_market_quote"
        ) as save_quote,
    ):
        result = await worker.run_once()

    assert result.instruments_processed == 2
    assert result.quotes_saved == 1
    assert result.quotes_failed == 1

    save_quote.assert_called_once()
    mock_db.close.assert_called_once()


@pytest.mark.anyio
async def test_worker_closes_session_when_database_read_fails(
    worker,
    mock_db,
):
    with (
        patch(
            "app.workers.market_data_worker.instrument_service.get_instruments",
            side_effect=RuntimeError("Database unavailable"),
        ),
        pytest.raises(RuntimeError, match="Database unavailable"),
    ):
        await worker.run_once()

    mock_db.close.assert_called_once()


@pytest.mark.anyio
async def test_worker_handles_empty_instrument_list(
    worker,
    mock_db,
):
    with patch(
        "app.workers.market_data_worker.instrument_service.get_instruments",
        return_value=[],
    ):
        result = await worker.run_once()

    assert result.instruments_processed == 0
    assert result.quotes_saved == 0
    assert result.quotes_failed == 0
    assert result.errors == ()

    mock_db.close.assert_called_once()


@pytest.mark.anyio
async def test_worker_handles_multiple_providers(
    worker,
    mock_db,
    mock_registry,
    mock_instrument,
):
    yahoo_provider = MagicMock()
    yahoo_provider.name = "yahoo"
    yahoo_provider.fetch_quote = AsyncMock(
        return_value=NormalizedQuote(
            symbol="BTCUSDT",
            provider="yahoo",
            bid=None,
            ask=None,
            last=Decimal("65050"),
            timestamp=datetime.now(UTC),
        )
    )

    mock_registry.list_providers.return_value = ["binance", "yahoo"]
    mock_registry.get.side_effect = [
        mock_registry.get.return_value,
        yahoo_provider,
    ]

    with (
        patch(
            "app.workers.market_data_worker.instrument_service.get_instruments",
            return_value=[mock_instrument],
        ),
        patch(
            "app.workers.market_data_worker.market_data_service.save_market_quote"
        ) as save_quote,
    ):
        result = await worker.run_once()

    assert result.instruments_processed == 1
    assert result.quotes_saved == 2
    assert result.quotes_failed == 0

    assert save_quote.call_count == 2
    mock_db.close.assert_called_once()
