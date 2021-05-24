import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.services.dependencies import get_token_header

from app.user_stocks import router as user_stocks_router
from app.finance import router as stocks_router
from app.news import router as news_router

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_stocks_router,
                   prefix="/api/user_stocks",
                   tags=["User stocks"],
                   dependencies=[Depends(get_token_header)],
                   responses={404: {"description": "Not found"}},
                   )

app.include_router(stocks_router,
                   prefix="/api/stocks",
                   tags=["Stocks"],
                   dependencies=[Depends(get_token_header)],
                   responses={404: {"description": "Not found"}},
                   )

app.include_router(news_router,
                   prefix="/api/news",
                   tags=["News"],
                   dependencies=[Depends(get_token_header)],
                   responses={404: {"description": "Not found"}},
                   )


@app.get('/_ah/warmup')
def warmup():
    return {'message': 'ok'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
