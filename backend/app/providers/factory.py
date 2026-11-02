from app.providers import (
    BinanceProvider,
    ProviderRegistry,
    YahooProvider,
)


def create_provider_registry() -> ProviderRegistry:
    registry = ProviderRegistry()

    registry.register(BinanceProvider())
    registry.register(YahooProvider())

    return registry
