import firebase_admin
from fastapi import HTTPException
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
from app.user_stocks.model import UserStocks

cred = credentials.Certificate('config/credentials/firestore_service_account.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def read_stocks(email):
    stocks_firebase = db.collection('stocks').document(email).get().to_dict()
    if stocks_firebase:
        return stocks_firebase
    else:
        stocks = UserStocks()
        stocks.stocks = []
        # stocks.titres = []
        return update_stocks(email, stocks)


def update_stocks(email, stocks):
    db.collection('stocks').document(email).set(stocks.dict())
    return read_stocks(email)
