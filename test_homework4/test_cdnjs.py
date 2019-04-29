"""tests for https://api.cdnjs.com, provide this URL in --addresss"""
import pytest

ENDPOINTS = [
    "libraries/jquery",
    "libraries?search=beaver&fields=assets",
    "libraries?output=human"
    ]

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_status_code(client_cdnjs, endpoint):
    """check status code of GET request"""
    response = client_cdnjs.do_get(endpoint)
    assert response.status_code == 200

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_header(client_cdnjs, endpoint):
    """check header of GET request"""
    response = client_cdnjs.do_get(endpoint)
    assert response.headers['content-encoding'] == 'gzip'

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_text(client_cdnjs, endpoint):
    """check contents of response"""
    response = client_cdnjs.do_get(endpoint)
    assert "name" in response.text

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_endpoints_post(client_cdnjs, endpoint):
    """check status code of a simple POST with no data"""
    response = client_cdnjs.do_post(endpoint)
    assert response.status_code == 404
