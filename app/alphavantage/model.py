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
