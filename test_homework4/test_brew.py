"""tests for https://api.openbrewerydb.org, provide this URL in --addresss"""
import pytest

ENDPOINTS = [
    "breweries",
    "breweries/search?query=beaver",
    "breweries?by_state=new_york",
    "breweries?by_tag=patio"
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
    assert response.headers['content-type'] == 'application/json; charset=utf-8'

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
