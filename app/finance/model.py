from pydantic import BaseModel
from typing import List, Optional


class DataStock(BaseModel):
    symbol: str
    # open: Optional[float]
    # high: Optional[float]
    # low: Optional[float]
    price: float
    # volume: Optional[int]
    # latest_trading_day: Optional[str]
    previous_close: float
    # change: Optional[float]
    # change_percent: Optional[str]


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
