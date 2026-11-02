from datetime import UTC, datetime
from decimal import Decimal, InvalidOperation

import httpx2

from app.providers.base import NormalizedQuote


class YahooProvider:
    """
    Proveedor de cotizaciones mediante Yahoo Finance REST API.
    """

    name = "yahoo"

    BASE_URL = "https://query1.finance.yahoo.com/v7/finance/quote"

    def __init__(
        self,
        client: httpx2.AsyncClient | None = None,
        timeout: float = 10.0,
    ) -> None:
        self._client = client
        self._timeout = timeout

    async def fetch_quote(self, symbol: str) -> NormalizedQuote:
        if not symbol or not symbol.strip():
            raise ValueError("Symbol cannot be empty")

        normalized_symbol = symbol.strip().upper()

        headers = {
            "User-Agent": "Mozilla/5.0",
        }

        if self._client is not None:
            return await self._request_quote(
                self._client,
                normalized_symbol,
            )

        async with httpx2.AsyncClient(
            timeout=self._timeout,
            headers=headers,
        ) as client:
            return await self._request_quote(
                client,
                normalized_symbol,
            )

    async def _request_quote(
        self,
        client: httpx2.AsyncClient,
        symbol: str,
    ) -> NormalizedQuote:

        response = await client.get(
            self.BASE_URL,
            params={"symbols": symbol},
        )

        response.raise_for_status()

        data = response.json()

        try:
            results = data["quoteResponse"]["result"]

            if not results:
                raise ValueError(f"No market data available for {symbol}")

            quote_data = results[0]

            if quote_data.get("symbol", "").upper() != symbol:
                raise ValueError("Yahoo returned an unexpected symbol")

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

            last = to_decimal(quote_data.get("regularMarketPrice"))

            bid = to_decimal(quote_data.get("bid"))

            ask = to_decimal(quote_data.get("ask"))

            if bid is not None and ask is not None and bid > ask:
                bid = None
                ask = None

            if last is None and bid is None and ask is None:
                raise ValueError(f"No valid prices available for {symbol}")

            timestamp = quote_data.get("regularMarketTime")

            market_timestamp = (
                datetime.fromtimestamp(timestamp, UTC)
                if timestamp is not None
                else datetime.now(UTC)
            )

            return NormalizedQuote(
                symbol=symbol,
                provider=self.name,
                bid=bid,
                ask=ask,
                last=last,
                timestamp=market_timestamp,
            )

        except (KeyError, IndexError, TypeError) as exc:
            raise ValueError(f"Invalid Yahoo Finance response for {symbol}") from exc
