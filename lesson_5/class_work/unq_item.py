list = input("Введите список целых чисел через запятую: ").split(" ")

uniq_it = set(list)
print("Уникальных элементов: ", len(uniq_it))