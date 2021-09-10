import pytest

def pytest_addoption(parser):
    """add commandline options"""
    parser.addoption('--env', action='store', default='PC',
                     help='pc or sp')

@pytest.fixture(scope="session", autouse=True)
def props(request):
    from TestProperties import TestProperties
    # return TestProperties(file_path='test_config.ini', section='TEST')
    return TestProperties(section=request.config.getoption("--env"))