from datetime import UTC, datetime
from decimal import Decimal, InvalidOperation

import yfinance as yf

from app.providers.base import NormalizedQuote


class YahooProvider:
    """
    Proveedor de cotizaciones mediante Yahoo Finance.
    """

    name = "yahoo"

    async def fetch_quote(self, symbol: str) -> NormalizedQuote:
        if not symbol or not symbol.strip():
            raise ValueError("Symbol cannot be empty")

        normalized_symbol = symbol.strip()
        ticker = yf.Ticker(normalized_symbol)

        info = ticker.fast_info

        last_value = info.get("lastPrice")
        bid_value = info.get("bid")
        ask_value = info.get("ask")

        def to_decimal(value) -> Decimal | None:
            if value is None:
                return None

            try:
                result = Decimal(str(value))
            except InvalidOperation, ValueError:
                return None

            if not result.is_finite() or result <= 0:
                return None

            return result

        last = to_decimal(last_value)
        bid = to_decimal(bid_value)
        ask = to_decimal(ask_value)

        if bid is not None and ask is not None and bid > ask:
            bid = None
            ask = None

        if last is None and bid is None and ask is None:
            raise ValueError(f"No valid market data available for {normalized_symbol}")

        return NormalizedQuote(
            symbol=normalized_symbol,
            provider=self.name,
            bid=bid,
            ask=ask,
            last=last,
            timestamp=datetime.now(UTC),
        )
