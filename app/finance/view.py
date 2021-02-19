from typing import List

from fastapi import APIRouter

from app.finance.controller import get_stock_from_yahoo, search_stocks, get_palmares, get_palmares_dividend
from app.finance.model import DataStock, SearchResult

router = APIRouter()


@router.get('', response_model=List[SearchResult])
async def search(q: str):
    return search_stocks(q)


@router.get('/palmares')
async def palmares():
    return get_palmares()


@router.get('/palmares_dividends')
async def palmares_dividends(page: int = 1):
    return get_palmares_dividend(1)


@router.get('/{stock}', response_model=DataStock)
async def get_stock(stock: str):
    return get_stock_from_yahoo(stock)