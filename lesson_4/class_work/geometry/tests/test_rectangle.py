import pytest

from lesson_4.class_work.geometry.func import *


def test_perim_rect():
    assert perim_rect(2, 3) == 10
    assert area_rect(2, 3) == 6


def test_area_rect():
    with pytest.raises(Exception):
        perim_rect("d")
        area_rect(-1)