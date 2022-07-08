import pytest

from lesson_4.class_work.my_function import sum_n, days_month


# def test_sum_n():
#     assert sum_n(5, 6) == 11

def test_days_month():
    assert type(days_month(3)) == int
    assert days_month(2) == 28
    assert days_month(3) == 31
    assert days_month(4) == 30


def test_days_month1():
    with pytest.raises(Exception):
        days_month("h")


def test_days_month2():
    with pytest.raises(Exception):
        days_month(13)
