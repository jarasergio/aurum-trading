from datetime import UTC, datetime
from decimal import Decimal

import httpx2
import pytest

from app.providers.yahoo import YahooProvider


def make_client(handler):
    transport = httpx2.MockTransport(handler)

    return httpx2.AsyncClient(
        transport=transport,
        base_url="https://query1.finance.yahoo.com",
    )


@pytest.mark.anyio
async def test_fetch_quote_returns_normalized_data():
    def handler(request):
        assert request.url.params["symbols"] == "GLD"

        return httpx2.Response(
            200,
            json={
                "quoteResponse": {
                    "result": [
                        {
                            "symbol": "GLD",
                            "regularMarketPrice": 250.50,
                            "bid": 250.40,
                            "ask": 250.60,
                            "regularMarketTime": 1735689600,
                        }
                    ]
                }
            },
        )

    async with make_client(handler) as client:
        provider = YahooProvider()

        # Inyectamos el transporte HTTP de prueba.
        provider.BASE_URL = str(client.base_url) + "/v7/finance/quote"

        # Sustituimos el cliente HTTP mediante el método de prueba.
        from unittest.mock import patch

        with patch("app.providers.yahoo.httpx2.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value = client
            mock_client.return_value.__aexit__.return_value = False

            quote = await provider.fetch_quote("GLD")

    assert quote.symbol == "GLD"
    assert quote.provider == "yahoo"
    assert quote.last == Decimal("250.5")
    assert quote.bid == Decimal("250.4")
    assert quote.ask == Decimal("250.6")
    assert quote.timestamp == datetime(2025, 1, 1, tzinfo=UTC)


@pytest.mark.anyio
async def test_fetch_quote_rejects_empty_symbol():
    provider = YahooProvider()

    with pytest.raises(ValueError, match="Symbol cannot be empty"):
        await provider.fetch_quote("")


@pytest.mark.anyio
async def test_fetch_quote_rejects_missing_prices():
    def handler(request):
        return httpx2.Response(
            200,
            json={
                "quoteResponse": {
                    "result": [
                        {
                            "symbol": "GLD",
                            "regularMarketPrice": None,
                            "bid": None,
                            "ask": None,
                            "regularMarketTime": 1735689600,
                        }
                    ]
                }
            },
        )

    async with make_client(handler) as client:
        provider = YahooProvider()
        provider.BASE_URL = str(client.base_url) + "/v7/finance/quote"

        from unittest.mock import patch

        with patch("app.providers.yahoo.httpx2.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value = client
            mock_client.return_value.__aexit__.return_value = False

            with pytest.raises(ValueError, match="No valid prices"):
                await provider.fetch_quote("GLD")


@pytest.mark.anyio
async def test_fetch_quote_propagates_http_errors():
    def handler(request):
        return httpx2.Response(500)

    async with make_client(handler) as client:
        provider = YahooProvider()
        provider.BASE_URL = str(client.base_url) + "/v7/finance/quote"

        from unittest.mock import patch

        with patch("app.providers.yahoo.httpx2.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value = client
            mock_client.return_value.__aexit__.return_value = False

            with pytest.raises(httpx2.HTTPStatusError):
                await provider.fetch_quote("GLD")
