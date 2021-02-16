from fastapi import APIRouter

from app.alphavantage.controller import get_stock_from_yahoo
from app.alphavantage.model import DataStock

router = APIRouter()


@router.get('/{stock}', response_model=DataStock)
async def get_stock(stock: str):
    return get_stock_from_yahoo(stock)
