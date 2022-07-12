string = input()
my_dict = {}
for i in range(len(set(string))):
    uniq = list(set(string))
    up = {uniq[i]: string.count(uniq[i])}
    print(up)
    my_dict.update(up)

print(my_dict)