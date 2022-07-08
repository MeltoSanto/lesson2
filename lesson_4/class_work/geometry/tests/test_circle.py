import pytest

from lesson_4.class_work.geometry.func import *


def test_perim_circ():
    assert round(perim_circ(15)) == 47
    assert round(area_circ(15)) == 177


def test_area_circ():
    with pytest.raises(Exception):
        perim_circ("d")
        area_circ(-1)