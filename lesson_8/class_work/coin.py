from random import randint
from statistics import mean

coin_mass = []
count = []

for a in range(1, 10):
    for i in range(1, 100):
        random_number = randint(1, 2)
        coin_mass.append(random_number)
        if random_number == 1:
            print("O", end=" ")
        else:
            print("P", end=" ")

        if int(len(coin_mass)) > 2 and coin_mass[-1] == coin_mass[-2] == coin_mass[-3]:
            count.append(i)
            print(f"(Попыток {i})")
            coin_mass = []
            break
# print(count)
print(f"\n"
      f"Максимально попыток - {max(count)}\n"
      f"Минимально попыток - {min(count)}\n"
      f"Среднее значение - {round(mean(count), 1)}")