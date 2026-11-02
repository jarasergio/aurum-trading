from datetime import UTC, datetime
from decimal import Decimal, InvalidOperation

import httpx

from app.providers.base import NormalizedQuote


class BinanceProvider:
    """
    Adaptador de Binance REST API.

    Obtiene bid, ask y last mediante endpoints públicos.
    """

    name = "binance"

    BASE_URL = "https://api.binance.com/api/v3"

    def __init__(
        self,
        client: httpx.AsyncClient | None = None,
        timeout: float = 10.0,
    ) -> None:
        self._client = client
        self._timeout = timeout

    async def fetch_quote(
        self,
        symbol: str,
    ) -> NormalizedQuote:
        normalized_symbol = symbol.strip().upper()

        if not normalized_symbol:
            raise ValueError("Symbol cannot be empty")

        if self._client is not None:
            return await self._request_quote(
                self._client,
                normalized_symbol,
            )

        async with httpx.AsyncClient(
            base_url=self.BASE_URL,
            timeout=self._timeout,
        ) as client:
            return await self._request_quote(
                client,
                normalized_symbol,
            )

    async def _request_quote(
        self,
        client: httpx.AsyncClient,
        symbol: str,
    ) -> NormalizedQuote:
        book_response = await client.get(
            f"{self.BASE_URL}/ticker/bookTicker",
            params={"symbol": symbol},
        )
        book_response.raise_for_status()

        price_response = await client.get(
            f"{self.BASE_URL}/ticker/price",
            params={"symbol": symbol},
        )
        price_response.raise_for_status()

        try:
            book_data = book_response.json()
            price_data = price_response.json()

            if not isinstance(book_data, dict):
                raise TypeError("Invalid Binance book response")

            if not isinstance(price_data, dict):
                raise TypeError("Invalid Binance book response")

            if book_data.get("symbol") != symbol or price_data.get("symbol") != symbol:
                raise ValueError("Binance returned an unexpected symbol")

            bid = Decimal(book_data["bidPrice"])
            ask = Decimal(book_data["askPrice"])
            last = Decimal(price_data["price"])

            return NormalizedQuote(
                symbol=symbol,
                provider=self.name,
                bid=bid,
                ask=ask,
                last=last,
                timestamp=datetime.now(UTC),
            )

        except (
            KeyError,
            TypeError,
            InvalidOperation,
        ) as exc:
            raise ValueError("Invalid market data received from Binance") from exc
