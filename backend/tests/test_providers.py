from datetime import UTC, datetime
from decimal import Decimal

import pytest

from app.providers.base import NormalizedQuote


def test_normalized_quote_accepts_valid_data():
    quote = NormalizedQuote(
        symbol="BTCUSDT",
        provider="binance",
        bid=Decimal("65000.00"),
        ask=Decimal("65001.00"),
        last=Decimal("65000.50"),
        timestamp=datetime.now(UTC),
    )

    assert quote.symbol == "BTCUSDT"
    assert quote.provider == "binance"
    assert quote.last == Decimal("65000.50")


def test_normalized_quote_rejects_naive_timestamp():
    with pytest.raises(ValueError, match="timezone"):
        NormalizedQuote(
            symbol="BTCUSDT",
            provider="binance",
            bid=Decimal(65000),
            ask=None,
            last=None,
            timestamp=datetime.now(),
        )


def test_normalized_quote_rejects_empty_prices():
    with pytest.raises(ValueError, match="At least one price"):
        NormalizedQuote(
            symbol="BTCUSDT",
            provider="binance",
            bid=None,
            ask=None,
            last=None,
            timestamp=datetime.now(UTC),
        )


def test_normalized_quote_rejects_invalid_spread():
    with pytest.raises(ValueError, match="Bid cannot be greater"):
        NormalizedQuote(
            symbol="BTCUSDT",
            provider="binance",
            bid=Decimal(65002),
            ask=Decimal(65001),
            last=None,
            timestamp=datetime.now(UTC),
        )
