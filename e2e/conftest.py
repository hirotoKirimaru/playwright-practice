import pytest

def pytest_addoption(parser):
    """add commandline options"""
    parser.addoption('--env', action='store', default='pc',
                     help='pc or sp')

@pytest.fixture(scope="session", autouse=True)
def props(request):
    from ScenarioProperties import ScenarioProperties
    # return TestProperties(file_path='test_config.ini', section='TEST')
    return ScenarioProperties(section=request.config.getoption("--env"))