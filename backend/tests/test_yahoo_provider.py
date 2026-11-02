from decimal import Decimal
from unittest.mock import MagicMock, patch

import pytest

from app.providers.yahoo import YahooProvider


@pytest.mark.anyio
async def test_fetch_quote_returns_normalized_data():
    provider = YahooProvider()

    mock_ticker = MagicMock()
    mock_ticker.fast_info = {
        "lastPrice": 250.50,
        "bid": 250.40,
        "ask": 250.60,
    }

    with patch(
        "app.providers.yahoo.yf.Ticker",
        return_value=mock_ticker,
    ):
        quote = await provider.fetch_quote("GLD")

    assert quote.symbol == "GLD"
    assert quote.provider == "yahoo"
    assert quote.last == Decimal("250.5")
    assert quote.bid == Decimal("250.4")
    assert quote.ask == Decimal("250.6")


@pytest.mark.anyio
async def test_fetch_quote_rejects_empty_symbol():
    provider = YahooProvider()

    with pytest.raises(ValueError, match="Symbol cannot be empty"):
        await provider.fetch_quote("")


@pytest.mark.anyio
async def test_fetch_quote_rejects_missing_prices():
    provider = YahooProvider()

    mock_ticker = MagicMock()
    mock_ticker.fast_info = {
        "lastPrice": None,
        "bid": None,
        "ask": None,
    }

    with (
        patch(
            "app.providers.yahoo.yf.Ticker",
            return_value=mock_ticker,
        ),
        pytest.raises(ValueError, match="No valid market data"),
    ):
        await provider.fetch_quote("GLD")
