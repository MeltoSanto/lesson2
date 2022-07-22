from math import *

from matplotlib import pyplot as plt
from matplotlib.pyplot import *


def discrem(a, b, c):
    disc = (b ** 2) - 4 * a * c
    return disc


def q_a(a, b, c):
    dsc = discrem(a, b, c)
    # print(dsc)
    if dsc < 0:
        print("Уравнение не имеет корней.")
    elif dsc == 0:
        x = (-b + sqrt(dsc)) / 2 * a
        print(f"Уравнение имеет один корень: {int(round(x))}.")
        draw_grapf_one(x)
    else:
        x1 = (-b + sqrt(dsc)) / 2 * a
        x2 = (-b - sqrt(dsc)) / 2 * a
        print(f"Уравнение имеет два корня: {round(x1, 2)} и {round(x2, 2)}.")
        draw_grapf(x1, x2, a, b, c)


def draw_grapf(x1, y1, a1, b1, c1):
    def f(x, a, b, c):
        return (a * x ** 2) + (b * x) + c

    x = int(round(x1))
    y = int(round(y1))

    x_coords = [x for x in range(x - 100, x + 100, 1)]

    y_coords = []
    for x in x_coords:
        y_coords.append(f(x, a1, b1, c1))

    print(x_coords)
    print(y_coords)

    plt.plot(x_coords, y_coords)
    plt.show()


def draw_grapf_one(a):
    x_coords = int(round(a))
    plt.plot(sin(x_coords))
    plt.show()
























