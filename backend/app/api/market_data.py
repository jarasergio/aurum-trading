from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.market_data import (
    MarketCandleResponse,
    MarketQuoteCreate,
    MarketQuoteResponse,
    MarketTickResponse,
)
from app.services import market_data_service

router = APIRouter(
    prefix="/market-data",
    tags=["Market Data"],
)


@router.post(
    "/quotes",
    response_model=MarketQuoteResponse,
    status_code=201,
)
def receive_quote(
    quote_data: MarketQuoteCreate,
    db: Annotated[Session, Depends(get_db)],
):
    try:
        return market_data_service.save_market_quote(
            db,
            quote_data,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.get(
    "/quotes/{instrument_id}",
    response_model=list[MarketQuoteResponse],
)
def list_latest_quotes(
    instrument_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    return market_data_service.get_latest_quotes(
        db,
        instrument_id,
    )


@router.get(
    "/ticks/{instrument_id}",
    response_model=list[MarketTickResponse],
)
def list_market_ticks(
    instrument_id: int,
    db: Annotated[Session, Depends(get_db)],
    provider: str | None = None,
    start_time: datetime | None = None,
    end_time: datetime | None = None,
    limit: Annotated[int, Query(ge=1, le=5000)] = 500,
):
    try:
        return market_data_service.get_market_ticks(
            db=db,
            instrument_id=instrument_id,
            limit=limit,
            provider=provider,
            start_time=start_time,
            end_time=end_time,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from exc


@router.get(
    "/candles/{instrument_id}",
    response_model=list[MarketCandleResponse],
)
def list_market_candles(
    instrument_id: int,
    timeframe: Annotated[str, Query(min_length=1, max_length=10)],
    db: Annotated[Session, Depends(get_db)],
    start_time: datetime | None = None,
    end_time: datetime | None = None,
    limit: Annotated[int, Query(ge=1, le=10000)] = 1000,
):
    try:
        return market_data_service.get_market_candles(
            db=db,
            instrument_id=instrument_id,
            timeframe=timeframe,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from exc
