def find_div(a):
    div = []
    for i in range(1, a):
        if a % i == 0:
            div.append(i)
    return div

def ideal(d, a):
    if sum(d) == a:
        print(f"Число {a} является совершенным.")
    else:
        print(f"Число {a} не совершенно.")

a = int(input("Введи число: "))
print(f"Делители числа '{a}' - {find_div(a)}")
ideal(find_div(a), a)
