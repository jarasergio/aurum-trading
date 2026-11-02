from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class MarketCandle(Base):
    __tablename__ = "market_candles"

    __table_args__ = (
        UniqueConstraint(
            "instrument_id",
            "provider",
            "timeframe",
            "open_time",
            name="uq_market_candles_instrument_provider_timeframe",
        ),
        CheckConstraint(
            "high >= low",
            name="ck_market_candles_high_low",
        ),
        CheckConstraint(
            "high >= open AND high >= close",
            name="ck_market_candles_high_open_close",
        ),
        CheckConstraint(
            "low <= open AND low <= close",
            name="ck_market_candles_low_open_close",
        ),
        Index(
            "ix_market_candles_instrument_time",
            "instrument_id",
            "timeframe",
            "open_time",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    instrument_id: Mapped[int] = mapped_column(
        ForeignKey("instruments.id", ondelete="CASCADE"),
        nullable=False,
    )

    provider: Mapped[str] = mapped_column(String(50), nullable=False)

    timeframe: Mapped[str] = mapped_column(String(10), nullable=False)

    open_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    close_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    open: Mapped[Decimal] = mapped_column(Numeric(28, 12), nullable=False)

    high: Mapped[Decimal] = mapped_column(Numeric(28, 12), nullable=False)

    low: Mapped[Decimal] = mapped_column(Numeric(28, 12), nullable=False)

    close: Mapped[Decimal] = mapped_column(Numeric(28, 12), nullable=False)

    volume: Mapped[Decimal | None] = mapped_column(Numeric(28, 12), nullable=True)
