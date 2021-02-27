from pydantic import BaseModel
from typing import List, Optional


class Stock(BaseModel):
    bought_value: float
    fullName: str
    qty: int
    symbol: str


class UserStocks(BaseModel):
    stocks: Optional[List[Stock]] = []
