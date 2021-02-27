from typing import List

from fastapi import APIRouter

from app.news.controller import get_news_for_stock, get_news
from app.news.model import News, CountryNews

router = APIRouter()


@router.get('/stock/{company}', response_model=List[News])
async def get_news_for_company(company: str):
    return get_news_for_stock(company)


@router.get('', response_model=List[CountryNews])
async def get_news_for_country(country: str = 'fr'):
    return get_news(country)
