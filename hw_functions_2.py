# *****************************************************************
# Б. Даны два числа n и m, n – размер вклада пользователя, m – срок вклада в годах.
# Вывести размер вклада n через m лет.
# Ставка - 10%.
# *****************************************************************

def calc_depos(n, m):
    s = (n * 10 * (365 * m) / 365) / 100
    d = n + s
    return d

n = input("Введите размер вклада: ")
m = int(input("Введите срок вклада (в годах): "))
cl_n = int(n.replace(' ', ''))

year = [1,21,31,41,51,61,71]
years = [2,3,4,22,23,24,32,33,34,42,43,44,52,53,54,62,63,64,72,73,74]
key_word = ''

if year.count(m):
    key_word = "год"
elif years.count(m):
    key_word = "года"
else:
    key_word = "лет"

print(f"Через {m} {key_word} вклад будет составлять - {calc_depos(cl_n, m)} рублей.")
