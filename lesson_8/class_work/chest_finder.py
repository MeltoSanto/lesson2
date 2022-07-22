num = ["1", "2", "3", "4", "5", "6", "7", "8"]
let = ["a", "b", "c", "d", "e", "f", "g", "h"]

res = input('Введите корды(маленькими буквами): ')
ress = list(res)

res_1 = num.index(ress[0])
res_2 = let.index(ress[1])

if res_1 % 2 == 0 and res_2 % 2 == 0:
    print("Клетка чёрная.")
else:
    print("Клетка белая.")