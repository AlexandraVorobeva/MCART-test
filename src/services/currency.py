import requests
from bs4 import BeautifulSoup


URL_RATE_BY_DAY = "http://www.cbr.ru/scripts/XML_daily.asp?"
URL_ALL_RATE = "http://www.cbr.ru/scripts/XML_valFull.asp"


def fetch_value_by_tag(soup, tag_of_value: str):
    """Fetch value by tag from soup object"""
    value = []
    value_with_tags = soup.find_all("{}".format(tag_of_value))
    for val in value_with_tags:
        val = str(val).replace("<{}>".format(tag_of_value), "")
        val = val.replace("</{}>".format(tag_of_value), "")
        value.append(val)
    return value


def fetch_all_currencies() -> dict:
    """Fetch dict of currencies of the world: name and character code."""
    page = requests.get(URL_ALL_RATE)
    soup = BeautifulSoup(page.text, "lxml")
    iso_char_code = fetch_value_by_tag(soup, "iso_char_code")
    names_of_currencies = fetch_value_by_tag(soup, "engname")
    all_currencies = dict(zip(iso_char_code, names_of_currencies))
    return all_currencies


def fetch_all_rate_by_day(day: str) -> dict:
    """Fetch exchange rate for all currencies by the day."""
    url1 = URL_RATE_BY_DAY + "date_req=" + str(day)
    page = requests.get(url1)
    soup = BeautifulSoup(page.text, "html.parser")
    rate_by_day_one = soup.find_all("valute")
    rate_by_day_one = list(rate_by_day_one)
    charcode = fetch_value_by_tag(soup, "charcode")
    all_currencies = dict(zip(charcode, rate_by_day_one))
    return all_currencies


def fetch_currency_value(currency: str, day: str) -> str:
    """Fetch value of exchange rate by the day."""
    day = day.split("-")
    day = day[2] + "/" + day[1] + "/" + day[0]
    all_rates_by_day = fetch_all_rate_by_day(day)
    rate = all_rates_by_day.get(currency)
    exchange_rates = rate.find_all("value")
    exchange_rates = str(exchange_rates).replace("[<value>", "")
    exchange_rates = exchange_rates.replace("</value>]", "")
    return exchange_rates


def compare_currency(currency: str, day1: str, day2: str) -> dict:
    """Getting the difference in the exchange rate between two dates."""
    exchange_rates = {}
    rate_day_one = fetch_currency_value(currency, day1)
    rate_day_two = fetch_currency_value(currency, day2)
    exchange_rates[day1] = rate_day_one
    exchange_rates[day2] = rate_day_two
    exchange_rates["difference"] = float(rate_day_one.replace(",", ".")) - float(
        rate_day_two.replace(",", ".")
    )
    return exchange_rates
