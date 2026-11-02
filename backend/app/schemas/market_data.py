from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class MarketQuoteCreate(BaseModel):
    instrument_id: int = Field(gt=0)
    provider: str = Field(min_length=1, max_length=50)

    bid: Decimal | None = Field(default=None, gt=0)
    ask: Decimal | None = Field(default=None, gt=0)
    last: Decimal | None = Field(default=None, gt=0)

    market_timestamp: datetime

    @model_validator(mode="after")
    def validate_prices(self):
        if self.bid is None and self.ask is None and self.last is None:
            raise ValueError("At least one price must be provided")

        if self.bid is not None and self.ask is not None and self.bid > self.ask:
            raise ValueError("Bid cannot be greater than ask")

        if self.market_timestamp.utcoffset() is None:
            raise ValueError("market_timestamp must include timezone")

        return self


class MarketQuoteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    instrument_id: int
    provider: str
    bid: Decimal | None
    ask: Decimal | None
    last: Decimal | None
    market_timestamp: datetime
    received_at: datetime


class MarketTickResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    instrument_id: int
    provider: str
    bid: Decimal | None
    ask: Decimal | None
    last: Decimal | None
    market_timestamp: datetime
    received_at: datetime


class MarketCandleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    instrument_id: int
    provider: str
    timeframe: str
    open_time: datetime
    close_time: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal | None
