import math
from math import *


def perim_circ(diam):
    perim = diam * pi
    perim = round(perim, 1)
    return perim

def perim_rect(s1, s2):
    perim = (s1 + s2) * 2
    return perim


def perim_tria(s1, s2, s3):
    perim = s1 + s2 + s3
    return perim


def area_circ(diam):
    area = diam ** 2 / 4 * pi
    area = round(area, 1)
    return area


def area_rect(s1, s2):
    area = s1 * s2
    return area


def area_tria(s1, s2, s3):
    p = (s1 + s2 + s3) / 2
    area = math.sqrt(p * (p - s1) * (p - s2) * (p - s3))
    return area


def real_figur():
    ...