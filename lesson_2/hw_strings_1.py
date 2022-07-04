# *****************************************************************
# А. Вводится n строк. Вывести количество пробелов
# *****************************************************************

main_string = ""
i = 0
counter_space = 0

kol_str = int(input(f"Введите кол-во строк: "))
print(f"Вводите предложения, в конце каждого нажимайте Enter: ")
for i in range(kol_str):
    main_string = main_string + input()
# while i < len(main_string):
#     if main_string[i] == " ":
#         counter_space += 1
#         i += 1
#     else:
#         i += 1
#         continue
print(f"Суммарно в этих предложениях: {main_string.count(' ')} пробел(ов).") #короткий вариант подсчёта пробелов в строках
#print(f"Суммарно в этих предложениях: {counter_space} пробелов.")