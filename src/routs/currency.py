from fastapi import APIRouter, HTTPException
import datetime
from ..services.currency import fetch_all_currencies, compare_currency
import requests_cache
from requests_cache import CachedSession


router = APIRouter(prefix="/currency")


session = CachedSession()
requests_cache.install_cache(expire_after=360, allowable_methods=('GET', 'POST'))


@router.get("/all")
def get_list_of_all_currencies():
    with requests_cache.enabled():
        return fetch_all_currencies()


@router.get("/difference")
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
