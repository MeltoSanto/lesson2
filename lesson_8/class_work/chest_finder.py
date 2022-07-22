num = ["1", "2", "3", "4", "5", "6", "7", "8"]
let = ["a", "b", "c", "d", "e", "f", "g", "h"]

res = input('Введите корды(маленькими буквами): ') #5b
ress = list(res)

res_1 = num.index(ress[1])
res_2 = let.index(ress[0])

if res_1 % 2 == res_2 % 2:
    print("Клетка чёрная.")
else:
    print("Клетка белая.")