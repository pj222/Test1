import pytest


@pytest.fixture(scope="module")
def fixture_code():
    print("fixture code")
    yield
    print("after execution")


@pytest.mark.smoke
def test_t1(fixture_code):
    print("test_t1_smoke")
    # assert ac!=="hello","these 2 values should not be same"


@pytest.mark.sanity
def test_t2(fixture_code):
    print("test_t2_sanity")
