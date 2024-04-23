import pytest


# Tests marked as regression tests
@pytest.mark.regression
def test_example1():
    print("A first test in the regression test suite")
    assert False, "This test will always fail..."


@pytest.mark.regression
def test_example2():
    print("A first test in the regression test suite")
    assert True, "This test will always pass..."
