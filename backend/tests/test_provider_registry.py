import pytest

from app.providers import (
    BinanceProvider,
    ProviderRegistry,
    YahooProvider,
)


def test_register_provider():
    registry = ProviderRegistry()

    registry.register(BinanceProvider())

    assert registry.list_providers() == ["binance"]


def test_get_provider():
    registry = ProviderRegistry()

    provider = BinanceProvider()
    registry.register(provider)

    assert registry.get("binance") is provider


def test_get_provider_is_case_insensitive():
    registry = ProviderRegistry()

    provider = BinanceProvider()
    registry.register(provider)

    assert registry.get("BINANCE") is provider


def test_register_duplicate_provider():
    registry = ProviderRegistry()

    registry.register(BinanceProvider())

    with pytest.raises(ValueError):
        registry.register(BinanceProvider())


def test_get_unknown_provider():
    registry = ProviderRegistry()

    with pytest.raises(ValueError):
        registry.get("unknown")


def test_unregister_provider():
    registry = ProviderRegistry()

    registry.register(YahooProvider())
    registry.unregister("yahoo")

    assert registry.list_providers() == []
