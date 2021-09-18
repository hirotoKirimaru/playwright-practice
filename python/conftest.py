import pytest
import os

def pytest_addoption(parser):
    """add commandline options"""
    parser.addoption('--env', 
                    action='store', 
                    default='IT',
                    help='pc or sp')
    parser.addoption('--local', 
                    action='store_true', 
                    default=False,
                    help='local')



@pytest.fixture(scope="session", autouse=True)
def props(request):
    from TestProperties import TestProperties

    os.environ['ENV'] = request.config.getoption("--env")
    print("*****")
    print(request.config.getoption("--local"))

    # return TestProperties(file_path='test_config.ini', section='TEST')
    return TestProperties(section=request.config.getoption("--env"))