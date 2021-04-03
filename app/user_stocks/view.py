from typing import Optional
from .controller import get_user_stocks, update_user_stocks
from fastapi import APIRouter, Header

from .model import UserStocks

router = APIRouter()


@router.get('', response_model=UserStocks)
async def get(x_goog_authenticated_user_email: Optional[str] = Header(None)):
    """
    Read all stock options
    :param x_goog_authenticated_user_email: email of the user making the call
    :return: list of user's stocks
    """
    print(f"current user: {x_goog_authenticated_user_email}")
    return get_user_stocks(x_goog_authenticated_user_email)


@router.patch('', response_model=UserStocks)
async def update(user_stocks: UserStocks, x_goog_authenticated_user_email: Optional[str] = Header(None)):
    """
    Update user's stock. Creates if does not exist. You need to send the all stocks each time.
    :param user_stocks: List of all user's stocks
    :param x_goog_authenticated_user_email: email of the user making the call
    :return: list of user's stocks
    """
    return update_user_stocks(x_goog_authenticated_user_email, user_stocks)
