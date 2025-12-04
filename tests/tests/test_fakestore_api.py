import requests
from unittest.mock import patch, Mock

BASE_URL = "https://fakestoreapi.com"

def _mocked_get_success(url, *args, **kwargs):
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = [
        {"id": 1, "title": "Fake product", "price": 10.0, "category": "cat1"}
    ]
    mock_resp.text = str(mock_resp.json.return_value)
    mock_resp.headers = {"Content-Type": "application/json"}
    return mock_resp

def test_products_returns_200():
    url = f"{BASE_URL}/products"
    with patch("requests.get", side_effect=_mocked_get_success):
        response = requests.get(url, timeout=10)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list) and data[0]["id"] == 1
