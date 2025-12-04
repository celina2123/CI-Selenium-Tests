import requests
import responses

BASE_URL = "https://fakestoreapi.com"

@responses.activate
def test_products_returns_200():
    url = f"{BASE_URL}/products?limit=1"
    responses.add(
        responses.GET,
        url,
        json=[{"id": 1, "title": "Fake product"}],
        status=200,
        headers={"Content-Type": "application/json"},
    )

    response = requests.get(url, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list) and data[0]["id"] == 1
