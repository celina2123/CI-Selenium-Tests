import requests

BASE_URL = "https://fakestoreapi.com"

def test_products_returns_200():
    response = requests.get(f"{BASE_URL}/products", timeout=10)
    assert response.status_code == 200
