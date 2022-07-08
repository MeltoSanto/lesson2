from func import *

figure = input("Выберите какую фигуру считаем. \n"
               "1 - Круг\n"
               "2 - Треугольник\n"
               "3 - Прямоугольник\n"
               ">>> ")

if figure == "1" or figure == "2" or figure == "3":
    figure = int(figure)
else:
    print("ОШИБКА: Не првильный выбор.")

if figure == 1:
    diam_circ = input("Введите диаметр круга: ")
    diam_circ = int(diam_circ)
    if diam_circ <= 0:
        print("Такую фигуру не считаем((")
    else:
        print(f"Периметр круга: {perim_circ(diam_circ)}.\n"
              f"Площадь круга: {area_circ(diam_circ)}.")


elif figure == 2:
    sides_tria = input("Введите три стороны треугольника через пробел: ")
    s_t = sides_tria.split()
    s_t = list(map(int, s_t))
    if s_t[0] <= 0 or s_t[1] <= 0 or s_t[2] <= 0:
        print("Такую фигуру не считаем((")
    elif s_t[0] + s_t[1] < s_t[2] or s_t[1] + s_t[2] < s_t[0] or  s_t[2] + s_t[0] < s_t[1]:
        print("Ну это уже перебор! Меняй размеры.")
    else:
        print(f"Периметр треугольника: {perim_tria(s_t[0], s_t[1], s_t[2])}.\n"
              f"Площадь треугольника: {area_tria(s_t[0], s_t[1], s_t[2])}.")


elif figure == 3:
    sides_rect = input("Введите две соседние стороны прямоугольника, через пробел: ")
    s_r = sides_rect.split()
    s_r = list(map(int, s_r))
    if s_r[0] <= 0 or s_r[1] <= 0:
        print("Такую фигуру не считаем((")
    else:
        print(f"Периметр прямоугольника: {perim_rect(s_r[0], s_r[1])}.\n"
              f"Площадь прямоугольника: {area_rect(s_r[0], s_r[1])}.")

