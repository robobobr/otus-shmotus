"""All the fixtures for the tests"""
import pytest

@pytest.fixture(scope="session", autouse=True)
def sessie(request):
    """Session fixture with autouse"""
    print('\nSession start')

    def post_sess():
        print('\nSession out')

    request.addfinalizer(post_sess)

@pytest.fixture(scope="module")
def run_at_startup():
    """Fixture for a module"""
    print('\nStartup_procedure()')

    def cleanup_procedure():
        print('Cleanup_procedures()')

    yield "Startup procedures are running"

    cleanup_procedure()

@pytest.fixture(scope="function", autouse=True)
def funcy_stuff(request):
    """Function fixture with autouse to show how dangerous autouse is, sorta"""
    print('\nAutouse is dangerous')

    def post_funcy():
        print('\nand you should beware')

    request.addfinalizer(post_funcy)
