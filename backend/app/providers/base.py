from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Protocol, runtime_checkable


@dataclass(frozen=True, slots=True)
class NormalizedQuote:
    """
    Formato común de cotización para todos los proveedores.
    """

    symbol: str
    provider: str
    bid: Decimal | None
    ask: Decimal | None
    last: Decimal | None
    timestamp: datetime

    def __post_init__(self) -> None:
        if not self.symbol.strip():
            raise ValueError("Symbol cannot be empty")

        if not self.provider.strip():
            raise ValueError("Provider cannot be empty")

        if self.bid is None and self.ask is None and self.last is None:
            raise ValueError("At least one price must be provided")

        if self.timestamp.utcoffset() is None:
            raise ValueError("Timestamp must include timezone")

        if self.bid is not None and self.bid <= 0:
            raise ValueError("Bid must be positive")

        if self.ask is not None and self.ask <= 0:
            raise ValueError("Ask must be positive")

        if self.last is not None and self.last <= 0:
            raise ValueError("Last price must be positive")

        if self.bid is not None and self.ask is not None and self.bid > self.ask:
            raise ValueError("Bid cannot be greater than ask")


@runtime_checkable
class MarketDataProvider(Protocol):
    """
    Contrato común de los proveedores de datos financieros.
    """

    name: str

    async def fetch_quote(
        self,
        symbol: str,
    ) -> NormalizedQuote:
        """
        Obtiene una cotización y la devuelve normalizada.
        """
        ...
