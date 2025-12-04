import requests

def test_products_returns_200():
url = "https://fakestoreapi.com/products?limit=1"
response = requests.get(url, timeout=10)
assert response.status_code == 200
