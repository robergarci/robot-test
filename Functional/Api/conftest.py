#configs.py
import pytest

def pytest_addoption(parser):
    parser.addoption('--env',
    dest='testenv',
    choices=["DEV","INT","VIDEDRESSING"],
    default='INT',
    help='Specify environment: "DEV", "INT", "VIDEDRESSING')

@pytest.fixture(scope='session')
def testenv(request):
    return request.config.option.testenv