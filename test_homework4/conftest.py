"""This is API testing configuration module"""
import requests
import pytest

class APIClient:
    """A client to do GET request for a provided url"""
    headers = {"accept":"text/html", "Content-type": "application/json"}

    def __init__(self, address='localhost'):
        self.address = address

    def do_get(self, endpoint, verify_ssl=False):
        """runs a GET request"""
        url = "/".join([self.address, endpoint])
        return requests.get(url, headers=self.headers, verify=verify_ssl)

    def do_post(self, endpoint, data=None, verify_ssl=False):
        """runs a POST request"""
        url = "/".join([self.address, endpoint])
        headers = self.headers
        return requests.post(url, data, headers=headers, verify=verify_ssl)

def pytest_addoption(parser):
    """adds command line option for API address"""
    parser.addoption("--address", action="store",
                     default="localhost", help="Select REST API to test.")

@pytest.fixture
def client(request):
    """returns an instance of APIClient class with user-defined API address"""
    return APIClient(request.config.getoption("--address"))
