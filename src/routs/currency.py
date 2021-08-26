import os
from fastapi import APIRouter, HTTPException, Request, Response
import datetime
from ..services.currency import fetch_all_currencies, compare_currency
from fastapi_redis_cache import cache


router = APIRouter(prefix="/currency")


@router.get("/all")
@cache(expire=360)
def get_list_of_all_currencies():
        return fetch_all_currencies()


@router.get("/difference")
@cache(expire=60)
def get_rub_difference(character_code_of_currency: str, day1: str, day2: str):
    """Getting the difference in the exchange rate (ruble) between two dates.

    Dates must be sent in the following format YYYY-MM-DD.

    Currency must be sent like character code: USD, EUR.
    """
    try:
        datetime.datetime.strptime(day2, '%Y-%m-%d') and datetime.datetime.strptime(day2, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(status_code=400, detail="Incorrect format of 'days'")
    return compare_currency(character_code_of_currency, day1, day2)

