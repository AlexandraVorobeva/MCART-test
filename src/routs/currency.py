from fastapi import APIRouter
from ..services.currency import fetch_all_currencies, compare_curreny


router = APIRouter(prefix="/currency")


@router.get("/all")
def get_list_of_all_currencies():
    """List of currencies of the world."""
    return fetch_all_currencies()


@router.get("/difference")
def get_rub_difference(character_code_of_currency: str, day1: str, day2: str):
    """Getting the difference in the exchange rate (ruble) between two dates.

    Dates must be sent in the following format YYYY-MM-DD.

    Currency must be sent like character code: USD, EUR.
    """
    return compare_curreny(character_code_of_currency, day1, day2)
