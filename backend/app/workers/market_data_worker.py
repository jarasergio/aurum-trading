import logging
from collections.abc import Callable
from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.providers.registry import ProviderRegistry
from app.schemas.market_data import MarketQuoteCreate
from app.services import instrument_service, market_data_service

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class WorkerResult:
    instruments_processed: int
    quotes_saved: int
    quotes_failed: int
    errors: tuple[str, ...]


class MarketDataWorker:
    """
    Worker responsable de consultar y persistir cotizaciones
    de los instrumentos activos mediante los proveedores registrados.
    """

    def __init__(
        self,
        registry: ProviderRegistry,
        session_factory: Callable[[], Session] | None = None,
    ) -> None:
        self._session_factory = session_factory or SessionLocal
        self._registry = registry

    async def run_once(self) -> WorkerResult:
        """
        Ejecuta un ciclo completo de actualización de cotizaciones.
        """

        db = self._session_factory()

        quotes_saved = 0
        quotes_failed = 0
        errors: list[str] = []

        try:
            instruments = instrument_service.get_instruments(db)
            providers = self._registry.list_providers()

            for instrument in instruments:
                for provider_name in providers:
                    try:
                        provider = self._registry.get(provider_name)

                        quote = await provider.fetch_quote(instrument.symbol)

                        if quote.symbol.upper() != instrument.symbol.upper():
                            raise ValueError(
                                f"Unexpected symbol received: {quote.symbol}"
                            )

                        if quote.provider.strip().lower() != provider_name.lower():
                            raise ValueError(
                                f"Unexpected provider received: {quote.provider}"
                            )

                        quote_data = MarketQuoteCreate(
                            instrument_id=instrument.id,
                            provider=provider_name,
                            bid=quote.bid,
                            ask=quote.ask,
                            last=quote.last,
                            market_timestamp=quote.timestamp,
                        )

                        market_data_service.save_market_quote(
                            db,
                            quote_data,
                        )

                        quotes_saved += 1

                        logger.info(
                            "Market quote saved: instrument=%s provider=%s",
                            instrument.symbol,
                            provider_name,
                        )

                    except Exception as exc:
                        quotes_failed += 1

                        error_message = f"{instrument.symbol} [{provider_name}]: {exc}"
                        errors.append(error_message)

                        logger.exception(
                            "Failed to update market quote: %s",
                            error_message,
                        )

            return WorkerResult(
                instruments_processed=len(instruments),
                quotes_saved=quotes_saved,
                quotes_failed=quotes_failed,
                errors=tuple(errors),
            )

        finally:
            db.close()
