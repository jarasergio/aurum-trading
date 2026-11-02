import asyncio
import contextlib
import logging
import signal

import httpx2

from app.core.config import settings
from app.providers.factory import create_provider_registry
from app.workers.market_data_worker import MarketDataWorker

logger = logging.getLogger(__name__)


async def run_worker(stop_event: asyncio.Event | None = None) -> None:
    if not settings.MARKET_DATA_WORKER_ENABLED:
        logger.info("Market data worker is disabled")
        return

    interval = settings.MARKET_DATA_POLL_INTERVAL

    if interval <= 0:
        raise ValueError("MARKET_DATA_POLL_INTERVAL must be positive")

    owns_stop_event = stop_event is None

    if stop_event is None:
        stop_event = asyncio.Event()

    loop = asyncio.get_running_loop()

    if owns_stop_event:
        for sig in (signal.SIGINT, signal.SIGTERM):
            with contextlib.suppress(NotImplementedError, RuntimeError):
                loop.add_signal_handler(sig, stop_event.set)

    headers = {
        "User-Agent": "AurumTrading/0.1",
    }

    timeout = httpx2.Timeout(10.0)

    async with httpx2.AsyncClient(
        timeout=timeout,
        headers=headers,
        limits=httpx2.Limits(
            max_connections=20,
            max_keepalive_connections=10,
        ),
    ) as client:
        registry = create_provider_registry(client)

        worker = MarketDataWorker(
            registry=registry,
        )

        logger.info(
            "Market data worker started. Interval: %s seconds",
            interval,
        )

        while not stop_event.is_set():
            try:
                result = await worker.run_once()

                logger.info(
                    "Market cycle completed: instruments=%s saved=%s failed=%s",
                    result.instruments_processed,
                    result.quotes_saved,
                    result.quotes_failed,
                )

            except Exception:
                logger.exception("Market data cycle failed")

            with contextlib.suppress(TimeoutError):
                await asyncio.wait_for(
                    stop_event.wait(),
                    timeout=interval,
                )

    logger.info("Market data worker stopped")


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    asyncio.run(run_worker())


if __name__ == "__main__":
    main()
