import requests

from app.services.yahoo import get_headers_for_yahoo
from config import NEWSAPI_KEY


def get_news_for_stock(stock_name):
    r = requests.get(f"https://query2.finance.yahoo.com/v1/finance/search?q={stock_name}&quotesCount=0&newsCount=5",
                     headers=get_headers_for_yahoo())
    return r.json()['news']


def get_news(country):
    r = requests.get(f"http://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={NEWSAPI_KEY}")
    res = r.json()
    if res['status'] == "ok":
        return res['articles']
