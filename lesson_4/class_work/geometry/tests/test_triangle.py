import pytest

from lesson_4.class_work.geometry.func import *


def test_perim_tria():
    assert perim_tria(2, 3, 4) == 9
    assert round(area_tria(2, 3, 4)) == 3


def test_area_tria():
    with pytest.raises(Exception):
        perim_tria("d")
        area_tria(0)