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
    """adds command line options for API address"""
    parser.addoption("--address_dogs", action="store",
                     default='https://dog.ceo/api', help="Select URL for dogs test.")
    parser.addoption("--address_cdnjs", action="store",
                     default='https://api.cdnjs.com', help="Select URL for cdnjs test.")
    parser.addoption("--address_brew", action="store",
                     default='https://api.openbrewerydb.org', help="Select URL for brew test.")

@pytest.fixture
def client_dogs(request):
    """returns an instance of APIClient class with user-defined API address"""
    return APIClient(request.config.getoption("--address_dogs"))

@pytest.fixture
def client_cdnjs(request):
    """returns an instance of APIClient class with user-defined API address"""
    return APIClient(request.config.getoption("--address_cdnjs"))

@pytest.fixture
def client_brew(request):
    """returns an instance of APIClient class with user-defined API address"""
    return APIClient(request.config.getoption("--address_brew"))
