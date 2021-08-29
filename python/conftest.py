import pytest

@pytest.fixture(scope="session")
def props():
    from TestProperties import TestProperties
    return TestProperties()