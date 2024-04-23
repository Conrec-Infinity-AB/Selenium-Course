import pytest

from assertpy import assert_that  # https://assertpy.github.io/docs.html


@pytest.mark.assertions
def test_assertions1():
    assert_that("foo").starts_with("f")


@pytest.mark.assertions
def test_assertions2():
    assert_that("123").is_digit()


@pytest.mark.assertions
def test_assertions3():
    assert_that("").is_empty()
