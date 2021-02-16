from ..services.firestore import read_stocks, update_stocks


def get_user_stocks(email):
    return read_stocks(email)


def update_user_stocks(email, user_stocks):
    return update_stocks(email, user_stocks)
