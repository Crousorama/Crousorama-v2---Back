from pydantic import BaseModel
from typing import List


class Stock(BaseModel):
    bought_value: float
    fullName: str
    qty: int
    symbol: str


class UserStocks(BaseModel):
    pea: List[Stock] = []
    titres: List[Stock] = []
