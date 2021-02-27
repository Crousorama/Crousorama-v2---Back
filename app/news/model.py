from typing import Optional

from pydantic import BaseModel


class News(BaseModel):
    uuid: str
    title: str
    publisher: str
    link: str
    providerPublishTime: int
    type: str


class Source(BaseModel):
    id: Optional[str]
    name: Optional[str]


class CountryNews(BaseModel):
    source: Source
    author: Optional[str]
    title: Optional[str]
    description: Optional[str]
    url: Optional[str]
    urlToImage: Optional[str]
    publishedAt: Optional[str]
    content: Optional[str]
