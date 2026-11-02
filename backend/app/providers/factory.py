import httpx2

from app.providers import (
    BinanceProvider,
    ProviderRegistry,
    YahooProvider,
)


def create_provider_registry(
    client: httpx2.AsyncClient,
) -> ProviderRegistry:
    registry = ProviderRegistry()

    registry.register(BinanceProvider(client))
    registry.register(YahooProvider(client))

    return registry
