from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.instruments import router as instruments_router
from app.api.market_data import router as market_data_router
from app.db.session import get_db

app = FastAPI(
    title="Aurum Trading API",
    description=(
        "Backend modular para análisis cuantitativo, "
        "trading algorítmico y gestión de mercados."
    ),
    version="0.1.0",
)


# Registro de rutas
app.include_router(instruments_router)
app.include_router(market_data_router)


@app.get("/", tags=["General"])
async def root():
    return {
        "application": "Aurum Trading",
        "status": "online",
        "version": "0.1.0",
        "trading_mode": "simulation",
    }


@app.get("/health", tags=["General"])
async def health():
    return {
        "status": "healthy",
    }


@app.get("/health/database", tags=["General"])
def database_health(
    db: Annotated[Session, Depends(get_db)],
):
    db.execute(text("SELECT 1"))

    return {
        "database": "connected",
        "status": "healthy",
    }
