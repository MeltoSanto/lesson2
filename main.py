"""a = input()
b = input()
c = input()

d = 0
f = 0
e = 0

if a < b and b < c:
    d = a
    f = b
    e = c
elif b < c and c < a:
    d = b
    f = c
    e = a
elif c < a and a < b:
    d = c
    f = a
    e = c
elif b < a and b < c:
    d = a
    f = b
    e = c

print(f"{d}\n{f}\n{e}")

a = 1
b = 2
c = 3

print(int(a))
print(int(b))
print(int(c))



if a <= b:
    print(c)
if b <= c:
    print(b)
if c >= a:
    print(a)
    """
#a = 2
#for i in range(0, 10):
#    print(i)



# i = 1
# while i < 6:
#     print(i)
#     i += 1



# a = int(input())
#
# for i in range(1, a+1):
#     if i % 2 == 0:
#         print(i)



# a = int(input())
# i = 0
# while i <= a:
#     i += 1
#     if a % i == 0:
#         print(i)



# def ads(v,c):
#     d = v + c
#     return d
#
# a = ads(3,5)
# print(a)

# *****************************************************************
# А. Вводится n строк. Вывести количество пробелов
# *****************************************************************

# main_string = ""
# i = 0
# counter_space = 0
#
# kol_str = int(input(f"Введите кол-во строк: "))
# print(f"Введите строки, в конце каждой нажимайте Enter: ")
# for i in range(kol_str):
#     main_string = main_string + input()
# # while i < len(main_string):
# #     if main_string[i] == " ":
# #         counter_space += 1
# #         i += 1
# #     else:
# #         i += 1
# #         continue
# print(f"Тут: {main_string.count(' ')}") #короткий вариант подсчёта пробелов в строках
# #print(f"Суммарно в этих строках: {counter_space} пробелов.")

# *****************************************************************
# Б. Вводится n строк, каждая строка – одно слово. Составить из них
# предложение с пробелами и точкой в конце.
# *****************************************************************

# main_string = []
# final_str = ""
# i = 0
# counter_space = 0
#
# kol_str = int(input(f"Введите кол-во строк: "))
# print(f"Введите слова по одному, в конце каждого нажимайте Enter: ")
# for i in range(kol_str):
#     a = input()
#     main_string.append(a)
# i = 0
# main_string[0] = main_string[0].capitalize() #увеличение первого символа в первом элем.
# main_string[kol_str-1] = main_string[kol_str-1].__add__(".")#добавляем точку в конце последнего элемента
# for i in range(kol_str):
#     final_str = final_str + main_string[i] + " "
# print(f"{final_str}") #короткий вариант подсчёта пробелов в строках