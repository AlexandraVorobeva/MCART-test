from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_get_list_of_all_currencies():
    response = client.get("/currency/all")
    assert response.status_code == 200, response.text


def test_get_rub_difference():
    response = client.get(
        "/currency/difference?character_code_of_currency=USD&day1=2021-08-05&day2=2019-08-05"
    )
    assert response.status_code == 200, response.text
    assert response.json() == {
        "2021-08-05": "72,7857",
        "2019-08-05": "64,6423",
        "difference": 8.1434,
    }
