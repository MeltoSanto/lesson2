a = int(input())
i = 1
while i <= a:
    if a % i == 0:
        print(i)
        i += 1
    else:
        i += 1
        continue