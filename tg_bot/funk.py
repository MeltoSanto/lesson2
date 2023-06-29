import re
import vk_api
import config
import time
import sqlite3
from sqlite3 import Error
from vk_api import ApiError
from os import system

session = vk_api.VkApi(token=config.vk_tkn)
vk = session.get_api()


def sql_connection():
    try:
        con = sqlite3.connect('data/main.db')
        return con
    except Error:
        print(Error)


def sql_create_table_friends(con, name_tab, ident):
    cur = con.cursor()
    sql_cmd = f"""CREATE TABLE {ident + name_tab} (id int PRIMARY KEY,user_id int,name text,lname text,count_subs int,count_friends int,last_seen int, count_posts int, raiting_id int)"""
    cur.execute(sql_cmd)
    con.commit()


def sql_create_table_subs(con, name_tab, ident):
    cur = con.cursor()
    sql_cmd = f"""CREATE TABLE {ident + name_tab} (id int PRIMARY KEY,user_id int,name text,lname text,count_subs int,count_friends int,last_seen int)"""
    cur.execute(sql_cmd)
    con.commit()


def sql_insert(con, entry, name_tab, ident):
    cur = con.cursor()
    cur.execute(f"""INSERT INTO {ident + name_tab} (id, user_id, name, lname, count_subs, count_friends, last_seen, count_posts, raiting_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", entry)
    con.commit()


def inp_symb(a): # тире для красивого списка команд
    aa = []
    for i in range(a):
        aa.append('-')
    return ''.join(aa)


def len_line_file():
    with open('data/id_friends.txt', 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
    return line_count


def get_my_id():
    my_id = vk.account.getProfileInfo()
    return my_id


def calculate_time_create_db(id, type):
    user_info = vk.users.get(user_id=id, fields="counters")

    if type == "friends":
        count = user_info[0]["counters"]["friends"]
    elif type == "subs":
        count = user_info[0]["counters"]["followers"]

    time_in_sec = count * 0.8

    ty_res = time.gmtime(time_in_sec)
    res = time.strftime(f"%H ч. %M м. %S сек.", ty_res)
    return res


def most_friendly_hmy(id):  # вывести количество друзей по id, и все id друзей
    list_friends = vk.friends.get(user_id=id)
    clear_list_friends = list_friends['items']
    print(list_friends['count'], clear_list_friends)


def get_subs_info(id):  # получаем info про подписчиков пользователя

    con = sql_connection()
    cur = con.cursor()

    cur.execute("""SELECT * FROM sqlite_master WHERE TYPE = 'table'""")
    tab = cur.fetchall()
    all_tab = []
    for table in tab:
        all_tab.append(table[1])

    try:
        count_subs = vk.users.getFollowers(user_id=id)
    except ApiError:
        print("Нет доступа к аккаунту(((")
        exit()
    iter = 0
    count = 0
    cnt = count_subs['count']
    string_id = str(id)


    if 's' + string_id in all_tab:
        print('Таблица пользователя уже существует. Обновление не требуется. Можете пробовать другие функции.')
    else:
        sql_create_table_subs(con, string_id, 's')
        while count <= cnt:
            list_subs = vk.users.getFollowers(user_id=id, offset=iter, count=1000, fields='last_seen, followers_count, blacklisted, can_access_closed')
            list_id_subs = list_subs['items']


            def get_foll_count(j):
                if 'followers_count' in list_id_subs[j]:
                    c_subs = list_id_subs[j]['followers_count']
                    return c_subs
                else:
                    c_subs_null = 0
                    return c_subs_null

            def get_last_seen(j):
                if 'last_seen' in list_id_subs[j]:
                    l_seen = list_id_subs[j]['last_seen']['time']
                    return l_seen
                else:
                    l_seen_null = 0
                    return l_seen_null

            def get_freids_count(id_user):
                try:
                    fr = vk.friends.get(user_id=id_user)
                    c_friends_user = fr['count']
                    return c_friends_user
                except ApiError:
                    c_friends_user_null = 0
                    return c_friends_user_null

            # ВК выдаёт список id только по 1000 значений за запрос,
            # следующий запрос нужно начинать с 1001 id_шника, поэтому приходится перебирать по 1000 элементов за проход

            if cnt > 1000:  # что бы не вылетало при переполнении счётчика, проверяем сначала
                if cnt - iter > 1000:  # если итерация не последняя и значение больше 1000, то цикл до 1000
                    for i in range(1000):
                        id_user = list_id_subs[i]['id']
                        name_user = str(list_id_subs[i]['first_name'])
                        lname_user = str(list_id_subs[i]['last_name'])
                        c_subs_user = get_foll_count(i)
                        c_friends_user = get_freids_count(id_user)
                        last_seen_user = get_last_seen(i)
                        entry = (count, id_user, name_user, lname_user, c_subs_user, c_friends_user, last_seen_user)
                        sql_insert(con, entry, string_id, 's')
                        count += 1
                        print(f"{count}: {id_user}")
                else:
                    if count >= cnt:  # если счётчик больше количества подписчиков, стопаем цикл
                        break
                    else:  # если итерация последняя и мы не знаем точно какое это значение, т.е. цикл меньше 1000, то значение цикла должно быть точным
                        for j in range(cnt - iter):
                            id_user = list_id_subs[j]['id']
                            name_user = str(list_id_subs[j]['first_name'])
                            lname_user = str(list_id_subs[j]['last_name'])
                            c_subs_user = get_foll_count(j)
                            c_friends_user = get_freids_count(id_user)
                            last_seen_user = get_last_seen(j)
                            entry = (count, id_user, name_user, lname_user, c_subs_user, c_friends_user, last_seen_user)
                            sql_insert(con, entry, string_id, 's')
                            count += 1
                            print(f"{count}: {id_user}")


            elif cnt < 1000:  # в другом случае если кол-во сабов меньше 1000 сразу, то делаем цикл по кол-ву сабов
                if count >= cnt:
                    break
                else:
                    for j in range(cnt):
                        id_user = list_id_subs[j]['id']
                        name_user = str(list_id_subs[j]['first_name'])
                        lname_user = str(list_id_subs[j]['last_name'])
                        c_subs_user = get_foll_count(j)
                        c_friends_user = get_freids_count(id_user)
                        last_seen_user = get_last_seen(j)
                        entry = (count, id_user, name_user, lname_user, c_subs_user, c_friends_user, last_seen_user)
                        sql_insert(con, entry, string_id, 's')
                        count += 1
                        print(f"{count}: {id_user}")
            else:
                break

            iter += 1000



def get_friends_info(id):
# def count_over_thousand:
    #     ...
    #
    #
    # def count_under_thousand:
    #     ...

    with open('data/id_friends.txt', 'w') as f:  # получаем id_шники друзей пользователя
        count_subs = vk.friends.get(user_id=id)
        iter = 0
        count = 0
        cnt = count_subs['count']

        while count <= cnt:
            list_frnds = vk.friends.get(user_id=id, offset=iter, count=1000)
            list_id_frnds = list_frnds['items']

            # ВК выдаёт список id только по 1000 значений за запрос,
            # следующий запрос нужно начинать с 1001 id_шника, поэтому приходится перебирать по 1000 элементов за проход

            if cnt > 1000:  # что бы не вылетало при переполнении счётчика, проверяем сначала
                if cnt - iter > 1000:  # если итерация не последняя и значение больше 1000, то цикл до 1000
                    for i in range(1000):
                        id_user = str(list_id_frnds[i])
                        f.writelines(id_user + "\n")
                        count += 1
                        print(f"{count}: {id_user}")
                else:
                    if count >= cnt:  # если счётчик больше количества подписчиков, стопаем цикл
                        break
                    else:  # если итерация последняя и мы не знаем точно какое это значение, т.е. цикл меньше 1000, то значение цикла должно быть точным
                        for j in range(cnt - iter):
                            id_user = str(list_id_frnds[j])
                            f.writelines(id_user + "\n")
                            count += 1
                            print(f"{count}: {id_user}")


            elif cnt < 1000:  # в другом случае если кол-во сабов меньше 1000 сразу, то делаем цикл по кол-ву сабов
                if count >= cnt:
                    break
                else:
                    for j in range(cnt):
                        id_user = str(list_id_frnds[j])
                        f.writelines(id_user + "\n")
                        count += 1
                        print(f"{count}: {id_user}")
            else:
                break

            iter += 1000

    con = sql_connection()
    cur = con.cursor()

    cur.execute("""SELECT * FROM sqlite_master WHERE TYPE = 'table'""")
    tab = cur.fetchall()
    all_tab = []
    for table in tab:
        all_tab.append(table[1])

    try:
        count_friends = vk.friends.get(user_id=id)
    except ApiError:
        print("Нет доступа к аккаунту(((")
        exit()
    iter = 0
    count = 0
    cnt = count_friends['count']
    string_id = str(id)


    if 'f'+string_id in all_tab:
        print('Таблица пользователя уже существует. Обновление не требуется. Можете пробовать другие функции.')
    else:
        sql_create_table_friends(con, string_id, 'f')
        while count <= cnt:
            list_friends = vk.friends.get(user_id=id, offset=iter, count=1000, fields='last_seen, followers_count, blacklisted')
            list_id_friends = list_friends['items']


            def get_foll_count(j):
                if 'followers_count' in list_id_friends[j]:
                    c_subs = list_id_friends[j]['followers_count']
                    return c_subs
                else:
                    c_subs_null = 0
                    return c_subs_null

            def get_last_seen(j):
                if 'last_seen' in list_id_friends[j]:
                    l_seen = list_id_friends[j]['last_seen']['time']
                    return l_seen
                else:
                    l_seen_null = 0
                    return l_seen_null

            def get_freids_count(id_user):
                try:
                    fr = vk.friends.get(user_id=id_user)
                    c_friends_user = fr['count']
                    return c_friends_user
                except ApiError:
                    c_friends_user_null = 0
                    return c_friends_user_null

            def get_count_posts_wall(id_user):
                try:
                    req_wall = vk.wall.get(owner_id=id_user, count=1)
                    count_posts = req_wall['count']
                    return count_posts
                except ApiError:
                    c_friends_user_null = 0
                    return c_friends_user_null


            def get_raiting_id_user(id):
                def check_polindrom(id):
                    if str(id) == str(id)[::-1]:
                        return 100
                    else:
                        return 0

                def check_repeat_digits(id):
                    # моё решение
                    a = 0
                    score = 0
                    score_mass = []
                    for i in str(id):
                        try:
                            if str(id)[a - 1] == i == str(id)[a + 1]:
                                score += 1
                            elif score > 0:
                                score_mass.append(score + 2)
                                score = 0
                            else:
                                a += 1
                                continue
                        except:
                            score_mass.append(score + 2)
                            score = 0
                            continue
                        a += 1

                    # решение со StackOverflow
                    score_mass = [len(obj[0]) for obj in re.findall(r"((\d)\2{1,9})", str(id))]

                    summs = sum(score_mass)

                    if len(score_mass) == 3 and summs == 9:
                        return summs * 9
                    elif len(score_mass) == 3 and summs == 8:
                        return summs * 5
                    elif len(score_mass) == 3 and summs == 7:
                        return summs * 3
                    elif len(score_mass) == 3 and summs == 6:
                        return summs * 2

                    elif len(score_mass) == 2 and summs == 8 or summs == 9:
                        return summs * 10
                    elif len(score_mass) == 2 and summs == 6 or summs == 7:
                        return summs * 7
                    elif len(score_mass) == 2 and summs == 5:
                        return summs * 5
                    elif len(score_mass) == 2 and summs == 4:
                        return summs

                    elif len(score_mass) == 1 and summs == 8 or summs == 9:
                        return summs * 14
                    elif len(score_mass) == 1 and summs == 6 or summs == 7:
                        return summs * 8
                    elif len(score_mass) == 1 and summs == 4 or summs == 5:
                        return summs * 4
                    elif len(score_mass) == 1 and summs == 2 or summs == 3:
                        return summs
                    else:
                        return 0

                def check_short(id):
                    if len(str(id)) == 5:
                        return 90
                    elif len(str(id)) == 4:
                        return 110
                    elif len(str(id)) == 3:
                        return 150
                    elif len(str(id)) == 2:
                        return 190
                    else:
                        return 0


                return check_polindrom(id)+check_repeat_digits(id)+check_short(id)

            # ВК выдаёт список id только по 1000 значений за запрос,
            # следующий запрос нужно начинать с 1001 id_шника, поэтому приходится перебирать по 1000 элементов за проход

            if cnt > 1000:  # что бы не вылетало при переполнении счётчика, проверяем сначала
                if cnt - iter > 1000:  # если итерация не последняя и значение больше 1000, то цикл до 1000
                    for i in range(1000):
                        id_user = list_id_friends[i]['id']
                        name_user = str(list_id_friends[i]['first_name'])
                        lname_user = str(list_id_friends[i]['last_name'])
                        c_subs_user = get_foll_count(i)
                        c_friends_user = get_freids_count(id_user)
                        last_seen_user = get_last_seen(i)
                        count_posts = get_count_posts_wall(id_user)
                        entry = (count, id_user, name_user, lname_user, c_subs_user, c_friends_user, last_seen_user, count_posts, get_raiting_id_user(id_user))
                        sql_insert(con, entry, string_id, 'f')
                        count += 1
                        print(f"{count}: {id_user}")
                else:
                    if count >= cnt:  # если счётчик больше количества подписчиков, стопаем цикл
                        break
                    else:  # если итерация последняя и мы не знаем точно какое это значение, т.е. цикл меньше 1000, то значение цикла должно быть точным
                        for j in range(cnt - iter):
                            id_user = list_id_friends[j]['id']
                            name_user = str(list_id_friends[j]['first_name'])
                            lname_user = str(list_id_friends[j]['last_name'])
                            c_subs_user = get_foll_count(j)
                            c_friends_user = get_freids_count(id_user)
                            last_seen_user = get_last_seen(j)
                            count_posts = get_count_posts_wall(id_user)
                            entry = (count, id_user, name_user, lname_user, c_subs_user, c_friends_user, last_seen_user, count_posts, get_raiting_id_user(id_user))
                            sql_insert(con, entry, string_id, 'f')
                            count += 1
                            print(f"{count}: {id_user}")


            elif cnt < 1000:  # в другом случае если кол-во сабов меньше 1000 сразу, то делаем цикл по кол-ву сабов
                if count >= cnt:
                    break
                else:
                    for j in range(cnt):
                        id_user = list_id_friends[j]['id']
                        name_user = str(list_id_friends[j]['first_name'])
                        lname_user = str(list_id_friends[j]['last_name'])
                        c_subs_user = get_foll_count(j)
                        c_friends_user = get_freids_count(id_user)
                        last_seen_user = get_last_seen(j)
                        count_posts = get_count_posts_wall(id_user)
                        entry = (count, id_user, name_user, lname_user, c_subs_user, c_friends_user, last_seen_user, count_posts, get_raiting_id_user(id_user))
                        sql_insert(con, entry, string_id, 'f')
                        count += 1
                        print(f"{count}: {id_user}")
            else:
                break

            iter += 1000


def names_with_id_users_for_file():
    with open('data/id_subs.txt', 'r') as f:
        a = 1
        all = 0
        for i in f:
            old = time.time()
            user = vk.users.get(user_ids=i)
            name = user[0]['first_name']
            lname = user[0]['last_name']
            leave = time.time() - old
            all += leave
            print(
                f"{a}: {name} {lname} - {round(leave, 5)} - {round(all / a, 4)}")  # номер, имя, фамилия, время на обработку(ВНО), среднее ВНО
            a += 1


def name_with_id_user(id, pad):
    # именительный – nom
    # родительный – gen
    # дательный – dat
    # винительный – acc
    # творительный – ins
    # предложный – abl
    user = vk.users.get(user_ids=id, fields='sex', name_case=pad)
    name = user[0]['first_name']
    lname = user[0]['last_name']
    if user[0]['sex'] == 1:
        sex = 'её'
    elif user[0]['sex'] == 2:
        sex = 'его'
    elif user[0]['sex'] == 0:
        sex = 'это'
    return name, lname, sex


def more_all_friends():
    with open('data/id_friends.txt', 'r') as f:
        num = 0
        counter = 0
        max_friends = {}

        for i in f:
            old = time.time()
            user = vk.users.get(user_ids=int(i), fields='counters')
            uuser = user[0]
            if 'counters' in uuser:
                if uuser['counters']['friends'] > counter:
                    counter = uuser['counters']['friends']
                    max_friends.clear()
                    max_friends[uuser['id']] = counter

            num += 1
            system("cls")
            print(
                f"Обработано: ({num}/{len_line_file()}). Примерное время: {round((len_line_file() * (time.time() - old)) - ((time.time() - old) * num), 2)} сек.")
            # all_time += time.time() - old # суммируем общее время
            # print(time.time() - old, round(all_time, 4)) # выводим время закраченное на операцию
        for key in max_friends.keys():
            print(
                f"У этого человека, самый популярный друг {name_with_id_user(key, 'nom')[0]} {name_with_id_user(key, 'nom')[1]} - {max_friends[key]} друзей.")


def ten_rating_fr(bot, message, id):
    con = sql_connection()
    cur = con.cursor()

    cur.execute(f"""SELECT name FROM sqlite_master WHERE TYPE = 'table'""")
    tabs = cur.fetchall()
    all_tabs = []
    for tab in tabs:
        all_tabs.append(tab[0])

    if 'f'+str(id) in all_tabs:
        cur.execute(f"""SELECT ROWID, user_id, name, lname, count_friends FROM {'f'+str(id)} ORDER BY count_friends DESC""")
        ten_best = cur.fetchall()
        count = 1

        bot.send_message(message.chat.id, f"{inp_symb(10)}\n"
                                          f"Рейтинг \"ТОП 10 самых дружелюбных друзей {name_with_id_user(id, 'gen')[0]} {name_with_id_user(id, 'gen')[1]}\".\n"
                                          f"{inp_symb(10)}")

        for stri in ten_best:
            if count < 6:
                bot.send_message(message.chat.id, f"На {count}-ом месте: {name_with_id_user(stri[1], 'nom')[0]} {name_with_id_user(stri[1], 'nom')[1]} - {stri[4]} друга")
                count += 1
            elif count >= 6:
                break
    else:
        selection = input(f"{name_with_id_user(id, 'gen')[0]} {name_with_id_user(id, 'gen')[1]} нет в базе данных.\n"
                          f"Хотите просканировать и добавить {name_with_id_user(id, 'gen')[2]} в базу?\n"
                          f"Примерное время ожидания - {calculate_time_create_db(id, 'friends')}\n0"
                          f"1 - ДА | 0 - НЕТ: ")
        if selection == '1':
            get_friends_info(id)
            ten_rating_fr(id)
        elif selection == '0':
            exit()

    con.close()


def my_place_in_ten_rating_fr(bot, message, id):
    con = sql_connection()
    cur = con.cursor()

    cur.execute(f"""SELECT name FROM sqlite_master WHERE TYPE = 'table'""")
    tabs = cur.fetchall()
    all_tabs = []
    for tab in tabs:
        all_tabs.append(tab[0])

    user_info = vk.users.get(user_id=id, fields="counters")
    count_fr = user_info[0]["counters"]["friends"]

    if 'f' + str(id) in all_tabs:
        cur.execute(
            f"""SELECT ROWID, user_id, name, lname, count_friends FROM {'f' + str(id)} WHERE count_friends > {count_fr} ORDER BY count_friends DESC""")
        best = cur.fetchall()

        bot.send_message(message.chat.id, f"{inp_symb(100)}\n"
                                          f"На каком месте {name_with_id_user(id, 'nom')[0]} {name_with_id_user(id, 'nom')[1]} в рейтинге дружелюбия\n"
                                          f"{inp_symb(100)}")

        bot.send_message(message.chat.id, f"{name_with_id_user(id, 'nom')[0]} {name_with_id_user(id, 'nom')[1]} на {len(best) + 1}-ом месте среди своих друзей")


    else:
        selection = input(f"{name_with_id_user(id, 'gen')[0]} {name_with_id_user(id, 'gen')[1]} нет в базе данных.\n"
                          f"Хотите просканировать и добавить {name_with_id_user(id, 'gen')[2]} в базу?\n"
                          f"Примерное время ожидания - {calculate_time_create_db(id, 'friends')}\n0"
                          f"1 - ДА | 0 - НЕТ: ")
        if selection == '1':
            get_friends_info(id)
            my_place_in_ten_rating_fr(id)
        elif selection == '0':
            exit()

    con.close()


def more_all_posts(bot, message, id):
    con = sql_connection()
    cur = con.cursor()

    cur.execute(f"""SELECT name FROM sqlite_master WHERE TYPE = 'table'""")
    tabs = cur.fetchall()
    all_tabs = []
    for tab in tabs:
        all_tabs.append(tab[0])

    if 'f' + str(id) in all_tabs:
        cur.execute(
            f"""SELECT ROWID, user_id, name, lname, count_posts FROM {'f' + str(id)} ORDER BY count_posts DESC""")
        ten_best = cur.fetchall()
        count = 1

        bot.send_message(message.chat.id, f"{inp_symb(60)}\n"
                                          f"Рейтинг \"Кто из друзей {name_with_id_user(id, 'gen')[0]} {name_with_id_user(id, 'gen')[1]} больше всего постит на стену\".\n"
                                          f"{inp_symb(60)}")

        for stri in ten_best:
            if count < 4:
                bot.send_message(message.chat.id, f"На {count} месте: {name_with_id_user(stri[1], 'nom')[0]} {name_with_id_user(stri[1], 'nom')[1]} - {stri[4]} пост(а) на стене.")
                count += 1
            elif count >= 4:
                break
    else:
        bot.send_message(message.chat.id, f"{name_with_id_user(id, 'gen')[0]} {name_with_id_user(id, 'gen')[1]} нет в базе данных.\n"
                                            f"Хотите просканировать и добавить {name_with_id_user(id, 'gen')[2]} в базу?\n"
                                            f"Примерное время ожидания - {calculate_time_create_db(id, 'friends')}\n"
                                            f"1 - ДА | 0 - НЕТ: ")
        # if selection == '1':
        #     get_friends_info(id)
        #     more_all_posts(id)
        # elif selection == '0':
        #     exit()

    con.close()


def cool_id_at_friends(bot, message, id):
    con = sql_connection()
    cur = con.cursor()

    cur.execute(f"""SELECT name FROM sqlite_master WHERE TYPE = 'table'""")
    tabs = cur.fetchall()
    all_tabs = []
    for tab in tabs:
        all_tabs.append(tab[0])

    if 'f' + str(id) in all_tabs:
        cur.execute(
            f"""SELECT ROWID, user_id, name, lname, raiting_id FROM {'f' + str(id)} ORDER BY raiting_id DESC""")
        ten_best = cur.fetchall()
        count = 1

        bot.send_message(message.chat.id, f"{inp_symb(60)}\n"
                                          f"Рейтинг \"У кого из друзей {name_with_id_user(id, 'gen')[0]} {name_with_id_user(id, 'gen')[1]} самый красивый ID\".\n"
                                          f"{inp_symb(60)}")

        for stri in ten_best:
            if count < 11:
                bot.send_message(message.chat.id, f"На {count} месте: {name_with_id_user(stri[1], 'nom')[0]} {name_with_id_user(stri[1], 'nom')[1]} - ID:{stri[1]} с оценкой {stri[4]} балла.")
                count += 1
            elif count >= 11:
                break
    else:
        selection = input(f"{name_with_id_user(id, 'gen')[0]} {name_with_id_user(id, 'gen')[1]} нет в базе данных.\n"
                          f"Хотите просканировать и добавить {name_with_id_user(id, 'gen')[2]} в базу?\n"
                          f"Примерное время ожидания - {calculate_time_create_db(id, 'friends')}\n0"
                          f"1 - ДА | 0 - НЕТ: ")
        if selection == '1':
            get_friends_info(id)
            cool_id_at_friends(id)
        elif selection == '0':
            exit()

    con.close()




# ten_rating_fr(61189)
# my_place_in_ten_rating_fr(61189)
# more_all_posts(61189)

# get_friends_info(24602301)





# 469181076 - 4 subs
# 5 - 36.113 subs
# 139882657 - my id

# get_subs_id(139882657)
