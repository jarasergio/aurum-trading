import asyncio
from datetime import UTC
from decimal import Decimal

import httpx
import pytest

from app.providers.binance import BinanceProvider


def make_client(handler):
    transport = httpx.MockTransport(handler)

    return httpx.AsyncClient(
        transport=transport,
        base_url="https://api.binance.com",
    )


def test_fetch_quote_returns_normalized_data():
    def handler(request):
        if request.url.path.endswith("bookTicker"):
            return httpx.Response(
                200,
                json={
                    "symbol": "BTCUSDT",
                    "bidPrice": "65000.10",
                    "askPrice": "65001.20",
                },
            )

        return httpx.Response(
            200,
            json={
                "symbol": "BTCUSDT",
                "price": "65000.50",
            },
        )

    async def run():
        async with make_client(handler) as client:
            provider = BinanceProvider(client)

            quote = await provider.fetch_quote("btcusdt")

            assert quote.symbol == "BTCUSDT"
            assert quote.provider == "binance"
            assert quote.bid == Decimal("65000.10")
            assert quote.ask == Decimal("65001.20")
            assert quote.last == Decimal("65000.50")
            assert quote.timestamp.utcoffset() is not None
            assert quote.timestamp.tzinfo == UTC

    asyncio.run(run())


def test_fetch_quote_rejects_empty_symbol():
    async def run():
        provider = BinanceProvider()

        with pytest.raises(ValueError):
            await provider.fetch_quote(" ")

    asyncio.run(run())


def test_fetch_quote_propagates_http_errors():
    def handler(request):
        return httpx.Response(500)

    async def run():
        async with make_client(handler) as client:
            provider = BinanceProvider(client)

            with pytest.raises(httpx.HTTPStatusError):
                await provider.fetch_quote("BTCUSDT")

    asyncio.run(run())


def test_fetch_quote_rejects_unexpected_symbol():
    def handler(request):
        return httpx.Response(
            200,
            json={
                "symbol": "ETHUSDT",
                "bidPrice": "2000",
                "askPrice": "2001",
            },
        )

    async def run():
        async with make_client(handler) as client:
            provider = BinanceProvider(client)

            with pytest.raises(ValueError):
                await provider.fetch_quote("BTCUSDT")

    asyncio.run(run())
