# *****************************************************************
# Б. Вводится n строк, каждая строка – одно слово. Составить из них
# предложение с пробелами и точкой в конце.
# *****************************************************************

main_string = []
final_str = ""
i = 0
counter_space = 0

kol_str = int(input(f"Введите кол-во строк: "))
print(f"Введите слова по одному, в конце каждого нажимайте Enter: ")
for i in range(kol_str):
    a = input()
    main_string.append(a)

main_string[0] = main_string[0].capitalize() # увеличение первого символа в первом элем.
main_string[kol_str-1] = main_string[kol_str-1].__add__(".") # добавляем точку в конце последнего элемента

# for i in range(kol_str):
#     final_str = final_str + main_string[i] + " "

final_str = ' '.join(main_string) # нашел способ покороче собрать строку
print(f"{final_str}")