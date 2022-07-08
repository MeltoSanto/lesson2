from my_function import sum_n, days_month
#
# a = int(input())
# b = int(input())
#
# print(sum_n(a, b))

a = input("Введите номер месяца: ")
y = int(a)
x = days_month(y)
print(f"В этом месяце {x} дней.")