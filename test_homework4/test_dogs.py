"""tests for https://dog.ceo/api, provide this URL in --addresss"""
import pytest

ENDPOINTS = [
    "breeds/list/all",
    "breeds/image/random",
    "breed/shiba/images",
    "breed/terrier/fox/images/random/3"
    ]

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_status_code(client, endpoint):
    """check status code of GET request"""
    response = client.do_get(endpoint)
    assert response.status_code == 200

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_header(client, endpoint):
    """check header of GET request"""
    response = client.do_get(endpoint)
    assert response.headers['content-type'] == 'application/json'

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_text(client, endpoint):
    """check contents of response"""
    response = client.do_get(endpoint)
    assert "message" in response.text

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_post(client, endpoint):
    """check status code of a simple POST with no data"""
    response = client.do_post(endpoint)
    assert response.status_code == 200
