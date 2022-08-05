# try:
#     f = open("files/text.txt")
#     try:
#         word = str()
#         count = 0
#         for line in f:
#             if len(line) > count:
#                 word = line
#                 count = len(line)
#         print(count, word)
#     finally:
#         f.close()
# except FileNotFoundError:
#     print("Такой файл не найден.")


# with open("files/text.txt") as f:
#     for i, line in enumerate(f):
#         if i == 4: # строки считаются от 0
#             print(line)


f = open('files/text.txt')
lns = max(f.readlines(), key=len) # ищем самое длинное по ключу=len
print(lns)
f.close()
print(f.closed) # проверка закрыт ли файл
