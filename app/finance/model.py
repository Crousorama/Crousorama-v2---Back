from pydantic import BaseModel
from typing import List, Optional


class DataStock(BaseModel):
    symbol: str
    price: float
    currency: str
    full_name: str
    previous_close: float
    validRanges: List[str]
    timestamps: List[int]
    prices: dict


class SearchResult(BaseModel):
    exchange: Optional[str]
    shortname: Optional[str]
    quoteType: Optional[str]
    symbol: Optional[str]
    index: Optional[str]
    score: Optional[float]
    typeDisp: Optional[str]
    longname: Optional[str]
    isYahooFinance: Optional[str]


class Palmares(BaseModel):
    indice: str
    meta: str
    value: str
    variation: str
