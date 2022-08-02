main_dict = {5: ['Иван', 'Иванович'],
             3: ['Сергей', 'Петрович', '4', '3', '3', '5', '2', '4', '4', '5', '1', '2', '4'],
             56: ['Павел', 'Грибоедов'],
             100: ['Игнат', 'Ибрагимов'],
             1: ['Август', 'Куратов']}


def inp_symb(a): # тире для красивого списка команд
    aa = []
    for i in range(a):
        aa.append('-')
    return ''.join(aa)


def cmd_lst():
    print(f"Список команд:\n"
          f"add <Имя> <Фамилия> {inp_symb(21)} добавить ученика\n"
          f"all {inp_symb(37)} список всех учеников\n"
          f"mark <ID ученика> <Оценка> {inp_symb(14)} добавить ученику оценку\n"
          f"edit <ID ученика> <Имя> <Фамилия> {inp_symb(7)} поменять ученику Имя Фамилию\n"
          f"delete(del) <ID ученика> {inp_symb(16)} удалить ученика\n"
          f"average(av) <ID ученика> {inp_symb(16)} список со средним баллом\n"
          f"help {inp_symb(36)} перечень доступных команд\n"
          f"exit {inp_symb(36)} выход из программы\n"
          f"->> ", end="")


def add(cmd_list):
    if len(main_dict) > 0: # если в списке есть ученики то ID нового будет <самый большой + 1>
        count = max(main_dict) + 1
        main_dict[count] = [cmd_list[1], cmd_list[2]]
        print(f"Ученик {cmd_list[1]} {cmd_list[2]} ID({count}) - добавлен в список.")
    else: # если нет, то начинаем с <ID 1>
        count = 1
        main_dict[count] = [cmd_list[1], cmd_list[2]]
        print(f"Ученик {cmd_list[1]} {cmd_list[2]} ID({count}) - добавлен в список.")


def all():
    if len(main_dict) > 0: # проверка наличия строк в списке
        ln = 1
        for k, v in main_dict.items():
            print(f"№{ln} - ID({k}) - {v}")
            ln += 1
    else: # если нет выводим...
        print("Список пуст.")


def mark(cmd_list):
    if int(cmd_list[1]) in main_dict: # есть ли в списке введённый ID
        prom = main_dict.get(int(cmd_list[1]))
        prom.append(str(cmd_list[2]))
        print(f"Ученику {prom[0]} {prom[1]} добавлена оценка {cmd_list[2]}.")
    else:
        print("Такого ID не существует.")


def edit(cmd_list):
    if int(cmd_list[1]) in main_dict: # есть ли в списке введённый ID
        prom = main_dict.get(int(cmd_list[1]))
        prm_0 = prom[0]
        prm_1 = prom[1]
        prom[0] = cmd_list[2]
        prom[1] = cmd_list[3]
        print(f"Ученик {prm_0} {prm_1} изменён на {cmd_list[2]} {cmd_list[3]}.")
    else:
        print("Такого ID не существует.")


def delete(cmd_list):
    if int(cmd_list[1]) in main_dict: # есть ли в списке введённый ID
        prom = main_dict.get(int(cmd_list[1]))
        main_dict.pop(int(cmd_list[1]))
        print(f"Ученик {prom[0]} {prom[1]} удалён из списка.")
    else:
        print("Такого ID не существует.")


def average(cmd_list):
    if int(cmd_list[1]) in main_dict: # есть ли в списке введённый ID
        if len(main_dict[int(cmd_list[1])]) > 2: # проверка есть ли у ученика оценки
            len_mas = len(main_dict[int(cmd_list[1])])
            prom = main_dict.get(int(cmd_list[1]))
            name = prom[0]
            sname = prom[1]
            sm = 0
            count = 0
            for i in range(2, len_mas, 1):
                sm += int(prom[i])
                count += 1
            print(f"Средний балл ученика {name} {sname}: {round(sm / count, 2)}.")
        else:
            print("У этого ученика нет оценок.")
    else:
        print("Такого ID не существует.")


def processing(cmd):
    a = 1
    while a == 1:
        cmd_list = cmd.split(' ')
        if cmd_list[0] == 'add':
            add(cmd_list)
            cmd = input(f"->> ")

        elif cmd_list[0] == 'all':
            all()
            cmd = input("->> ")

        elif cmd_list[0] == 'mark':
            mark(cmd_list)
            cmd = input("->> ")

        elif cmd_list[0] == 'edit':
            edit(cmd_list)
            cmd = input("->> ")

        elif cmd_list[0] == 'delete' or cmd_list[0] == 'del':
            delete(cmd_list)
            cmd = input("->> ")

        elif cmd_list[0] == 'average' or cmd_list[0] == 'av':
            average(cmd_list)
            cmd = input("->> ")

        elif cmd_list[0] == 'help':
            cmd_lst()
            cmd = input()

        elif cmd_list[0] == 'exit':
            print("Выполнение программы окончено.")
            break

        else:
            print("ОШИБКА: Введите команду корректно.")
            cmd = input("->> ")
