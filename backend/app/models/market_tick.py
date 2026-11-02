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
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class MarketTick(Base):
    __tablename__ = "market_ticks"

    __table_args__ = (
        CheckConstraint(
            "bid IS NOT NULL OR ask IS NOT NULL OR last IS NOT NULL",
            name="ck_market_ticks_has_price",
        ),
        Index(
            "ix_market_ticks_instrument_timestamp",
            "instrument_id",
            "market_timestamp",
        ),
        Index(
            "ix_market_ticks_received_at",
            "received_at",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    instrument_id: Mapped[int] = mapped_column(
        ForeignKey("instruments.id", ondelete="CASCADE"),
        nullable=False,
    )

    provider: Mapped[str] = mapped_column(String(50), nullable=False)

    bid: Mapped[Decimal | None] = mapped_column(Numeric(28, 12), nullable=True)

    ask: Mapped[Decimal | None] = mapped_column(Numeric(28, 12), nullable=True)

    last: Mapped[Decimal | None] = mapped_column(Numeric(28, 12), nullable=True)

    market_timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    received_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
