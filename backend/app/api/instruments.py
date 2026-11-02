from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.instrument import (
    InstrumentCreate,
    InstrumentResponse,
    InstrumentUpdate,
)
from app.services import instrument_service

router = APIRouter(
    prefix="/instruments",
    tags=["Instruments"],
)


@router.get(
    "/",
    response_model=list[InstrumentResponse],
)
def list_instruments(
    db: Annotated[Session, Depends(get_db)],
):
    return instrument_service.get_instruments(db)


@router.get(
    "/{instrument_id}",
    response_model=InstrumentResponse,
)
def read_instrument(
    instrument_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    instrument = instrument_service.get_instrument(db, instrument_id)

    if instrument is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Instrument not found",
        )

    return instrument


@router.post(
    "/",
    response_model=InstrumentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_instrument(
    instrument_data: InstrumentCreate,
    db: Annotated[Session, Depends(get_db)],
):
    try:
        return instrument_service.create_instrument(db, instrument_data)
    except IntegrityError as err:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Instrument symbol already exists",
        ) from err


@router.patch(
    "/{instrument_id}",
    response_model=InstrumentResponse,
)
def update_instrument(
    instrument_id: int,
    instrument_data: InstrumentUpdate,
    db: Annotated[Session, Depends(get_db)],
):
    instrument = instrument_service.get_instrument(db, instrument_id)

    if instrument is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Instrument not found",
        )

    return instrument_service.update_instrument(
        db,
        instrument,
        instrument_data,
    )


@router.delete(
    "/{instrument_id}",
    response_model=InstrumentResponse,
)
def delete_instrument(
    instrument_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    instrument = instrument_service.get_instrument(db, instrument_id)

    if instrument is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Instrument not found",
        )

    return instrument_service.deactivate_instrument(db, instrument)
