import pytest

from lesson_4.home_work.task_1.func import discrem

def test_discrem_pos():
    assert discrem(1, 2, 3) == -8
    assert discrem(-11, -22, -33) == -968
    assert discrem(1, 1, 0) == 1

def test_discrem_neg():
    with pytest.raises(Exception):
        discrem("a", "b", "c")