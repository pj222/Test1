import pytest

@pytest.mark.smoke
def test_t3():
    print("test_t3_smoke")

@pytest.mark.sanity
def test_t4():
    print("test_t4_sanity")
    print("test_t4_sanity_10thmay")