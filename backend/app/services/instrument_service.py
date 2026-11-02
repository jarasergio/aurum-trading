from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.instrument import Instrument
from app.schemas.instrument import InstrumentCreate, InstrumentUpdate


def get_instruments(db: Session) -> list[Instrument]:
    statement = (
        select(Instrument).where(Instrument.is_active.is_(True)).order_by(Instrument.id)
    )
    return list(db.scalars(statement).all())


def get_instrument(db: Session, instrument_id: int) -> Instrument | None:
    return db.get(Instrument, instrument_id)


def create_instrument(
    db: Session,
    instrument_data: InstrumentCreate,
) -> Instrument:
    instrument = Instrument(**instrument_data.model_dump())

    db.add(instrument)
    db.commit()
    db.refresh(instrument)

    return instrument


def update_instrument(
    db: Session,
    instrument: Instrument,
    instrument_data: InstrumentUpdate,
) -> Instrument:
    update_data = instrument_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(instrument, field, value)

    db.commit()
    db.refresh(instrument)

    return instrument


def deactivate_instrument(
    db: Session,
    instrument: Instrument,
) -> Instrument:
    instrument.is_active = False

    db.commit()
    db.refresh(instrument)

    return instrument
