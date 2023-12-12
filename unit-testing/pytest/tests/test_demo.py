from app.demo import add, multiply, divide, discount_reason_condition
import pytest


@pytest.mark.skip("skipping this test")
def test_add():
    assert add(10, 23) == 33


@pytest.mark.skipif(discount_reason_condition(), reason="skipping due to discount reason")
def test_multiply():
    assert multiply(10, 23) == 230


def test_div():
    assert divide(40, 4) == 10
    with pytest.raises(ValueError):
        divide(4, 0)
