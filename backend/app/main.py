import asyncio
import contextlib
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.instruments import router as instruments_router
from app.api.market_data import router as market_data_router
from app.core.config import settings
from app.db.session import get_db
from app.workers.runner import run_worker


@asynccontextmanager
async def lifespan(app: FastAPI):
    stop_event = asyncio.Event()
    worker_task = None

    if settings.MARKET_DATA_WORKER_ENABLED:
        worker_task = asyncio.create_task(
            run_worker(stop_event),
            name="market-data-worker",
        )

    yield

    if worker_task is not None:
        stop_event.set()

        try:
            await asyncio.wait_for(
                worker_task,
                timeout=15,
            )
        except TimeoutError:
            worker_task.cancel()

            with contextlib.suppress(asyncio.CancelledError):
                await worker_task


app = FastAPI(
    title="Aurum Trading API",
    description=(
        "Backend modular para análisis cuantitativo, "
        "trading algorítmico y gestión de mercados."
    ),
    version="0.1.0",
    lifespan=lifespan,
)


app.include_router(instruments_router)
app.include_router(market_data_router)


@app.get("/", tags=["General"])
async def root():
    return {
        "application": "Aurum Trading",
        "status": "online",
        "version": "0.1.0",
        "trading_mode": settings.TRADING_MODE,
    }


@app.get("/health", tags=["General"])
async def health():
    return {
        "status": "healthy",
    }


@app.get("/health/database")
def database_health(
    db: Annotated[Session, Depends(get_db)],
):
    db.execute(text("SELECT 1"))

    return {
        "database": "connected",
        "status": "healthy",
    }
