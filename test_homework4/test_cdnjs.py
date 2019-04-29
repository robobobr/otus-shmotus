"""tests for https://api.cdnjs.com, provide this URL in --addresss"""
import pytest

ENDPOINTS = [
    "libraries/jquery",
    "libraries?search=beaver&fields=assets",
    "libraries?output=human"
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
    assert response.headers['content-encoding'] == 'gzip'

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_text(client, endpoint):
    """check contents of response"""
    response = client.do_get(endpoint)
    assert "name" in response.text

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_post(client, endpoint):
    """check status code of a simple POST with no data"""
    response = client.do_post(endpoint)
    assert response.status_code == 404
