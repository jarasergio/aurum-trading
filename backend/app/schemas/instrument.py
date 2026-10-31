
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class InstrumentCreate(BaseModel):
    symbol: str = Field(min_length=1, max_length=32)
    name: str = Field(min_length=1, max_length=120)
    asset_class: str = Field(min_length=1, max_length=30)
    market: str = Field(min_length=1, max_length=30)
    base_currency: str | None = Field(default=None, max_length=12)
    quote_currency: str | None = Field(default=None, max_length=12)


class InstrumentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    asset_class: str | None = Field(default=None, min_length=1, max_length=30)
    market: str | None = Field(default=None, min_length=1, max_length=30)
    base_currency: str | None = Field(default=None, max_length=12)
    quote_currency: str | None = Field(default=None, max_length=12)
    is_active: bool | None = None


class InstrumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    symbol: str
    name: str
    asset_class: str
    market: str
    base_currency: str | None
    quote_currency: str | None
    is_active: bool
    created_at: datetime
