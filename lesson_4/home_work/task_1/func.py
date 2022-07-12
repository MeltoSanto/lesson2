from math import sqrt


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
        print(f"Уравнение имеет один корень: {x}.")
    else:
        x1 = (-b + sqrt(dsc)) / 2 * a
        x2 = (-b - sqrt(dsc)) / 2 * a
        print(f"Уравнение имеет два корня: {round(x1, 2)} и {round(x2, 2)}.")