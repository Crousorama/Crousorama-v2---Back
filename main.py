from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.services.dependencies import get_token_header

from app.user_stocks import router as user_stocks_router
from app.alphavantage import router as stocks_router

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

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
