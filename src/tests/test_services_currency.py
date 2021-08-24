import pytest
import os
from bs4 import BeautifulSoup
from src.services.currency import (
    fetch_value_by_tag,
    fetch_all_rate_by_day,
    fetch_currency_value,
    compare_currency,
)


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "test_data.xml"), ["AUD", "ATS"]),
        (os.path.join(os.path.dirname(__file__), "test_data2.xml"), ["AZN", "GBP"]),
    ],
)
def test_fetch_value_by_tag(data, expected_result):
    with open(data) as file:
        src = file.read()
        soup = BeautifulSoup(src, "lxml")
        assert fetch_value_by_tag(soup, "iso_char_code") == expected_result


def test_fetch_all_rate_by_day_type(day="19/06/2021"):
    assert type(fetch_all_rate_by_day(day)) == dict


@pytest.mark.parametrize(
    ["currency", "day", "expected_result"],
    [
        ("USD", "2021-06-19", "72,2216"),
        ("USD", "2020-06-19", "69,6180"),
    ],
)
def test_fetch_currency_value(currency, day, expected_result):
    assert fetch_currency_value(currency, day) == expected_result


def test_compare_currency(currency="USD", day1="2021-06-19", day2="2020-06-19"):
    assert compare_currency(currency, day1, day2) == {
        "2021-06-19": "72,2216",
        "2020-06-19": "69,6180",
        "difference": 2.6036,
    }
