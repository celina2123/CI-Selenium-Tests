import requests

BASE_URL = "https://fakestoreapi.com"

def test_products_returns_200():
    url = f"{BASE_URL}/products?limit=1"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200
