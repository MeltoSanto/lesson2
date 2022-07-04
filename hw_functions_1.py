# *****************************************************************
# А. Написать функцию, которая принимает два числа и строку. Строка – один из “+”, “-”, “*”, “/”.
# Считать из ввода два числа и строку, вывести результат операции.
# *****************************************************************
import sys

i = 0
symb = 0
old_a = input(f"Введите арифметический пример.\nИспользуйте +, -, * или / для указания выполняемой операции: ")
a = old_a.replace(' ', '')
s = list(a)
# print(s, len(s))

symb = a.find("+")
if symb <= 0:
    symb = a.find("-")

if symb <= 0:
    symb = a.find("*")

if symb <= 0:
    symb = a.find("/")

act = s[symb]
ex = 0
# print(symb, type(symb))

x = int(''.join(s[0:symb]))
y = int(''.join(s[symb+1:len(s)]))
if y == 0 and act == '/':
    print("ОШИБКА: Замените ноль на другое число.")
    sys.exit()

if act == '+':
    ex = x + y
    int(ex)
elif act == '-':
    ex = x - y
    int(ex)
elif act == '*':
    ex = x * y
    int(ex)
elif act == '/':
    ex = x / y

print(f'{x} {act} {y} = {ex}')
