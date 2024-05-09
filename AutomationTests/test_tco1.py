import pytest
ac="hello"
@pytest.mark.smoke
def test_t1():
    print("test_t1_smoke")
    assert ac!= "hello","these 2 values should not be same"

@pytest.mark.sanity
def test_t2():
    print("test_t2_sanity")
    print("test_t2_sanity_gittest")