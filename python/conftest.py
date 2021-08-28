import pytest

@pytest.fixture
def props():
    from TestProperties import TestProperties
    return TestProperties()