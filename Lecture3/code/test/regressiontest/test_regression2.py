import pytest


# Tests marked as regression tests
@pytest.mark.regression
def test_example3():
    print("A third test in the regression test suite but in another file")
    assert True, "This test will always pass..."
