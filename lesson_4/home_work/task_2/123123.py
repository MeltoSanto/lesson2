import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(-10, 10)  # задаем диапазон по x

l = [int(x) for x in input().split()]

A = int(l[0])

B = int(l[1])

C = int(l[2])

y = A * x ** 2 + B * x + C

print('x - ', x)
print('y - ', y)


plt.plot(x, y)

plt.show()