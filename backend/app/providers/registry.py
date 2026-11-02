from app.providers.base import MarketDataProvider


class ProviderRegistry:
    """
    Registro centralizado de proveedores de datos de mercado.
    """

    def __init__(self) -> None:
        self._providers: dict[str, MarketDataProvider] = {}

    def register(self, provider: MarketDataProvider) -> None:
        name = provider.name.strip().lower()

        if not name:
            raise ValueError("Provider name cannot be empty")

        if name in self._providers:
            raise ValueError(f"Provider already registered: {name}")

        self._providers[name] = provider

    def get(self, name: str) -> MarketDataProvider:
        normalized_name = name.strip().lower()

        try:
            return self._providers[normalized_name]
        except KeyError as exc:
            raise ValueError(f"Provider not registered: {normalized_name}") from exc

    def list_providers(self) -> list[str]:
        return sorted(self._providers.keys())

    def unregister(self, name: str) -> None:
        normalized_name = name.strip().lower()

        if normalized_name not in self._providers:
            raise ValueError(f"Provider not registered: {normalized_name}")

        del self._providers[normalized_name]
