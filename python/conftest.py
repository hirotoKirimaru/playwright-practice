import pytest

@pytest.fixture(scope="session")
def props():
    from TestProperties import TestProperties
    # return TestProperties(file_path='test_config.ini', section='TEST')
    return TestProperties()