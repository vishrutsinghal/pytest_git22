import pytest
import calc2
# from pytest_calc.calc.calc import *
# from calc import *

NUMBER_1 = 30
NUMBER_2 = 60


def test_Add():
    value = calc.add(NUMBER_1, NUMBER_2)
    assert value == 90


def test_Sub():
    value = calc.sub(NUMBER_1, NUMBER_2)
    assert value == -30


def test_mul():
    value = calc.mul(NUMBER_1, NUMBER_2)
    assert value == 1800


def test_div():
    value = calc.div(NUMBER_1, NUMBER_2)
    assert value == 0.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        calc.div(NUMBER_1, 0)
    assert "division by 0", str(e)
