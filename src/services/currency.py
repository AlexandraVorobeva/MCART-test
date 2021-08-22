from requests import request
from bs4 import BeautifulSoup


BASE_URL = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="

def fetch_all_rate_by_day(day):
    url = BASE_URL + str(day)   #22/08/2021
    page = request("get", url)
    soup = BeautifulSoup(page.text, "lxml")
    ...
