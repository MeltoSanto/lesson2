import time
import timeit
from collections import Counter
import re

# import telebot

# import mysql.connector
import config
import vk_api
# from pyfacebook import GraphAPI
# from instabot import Bot
#
# # token = "vk1.a.CoZIh70v9fLG-X83dPlPW8wzpdrfJi30C3t5k1seOVx0CLCN5RBUWEbvqk_XvfVwaVx4g4MnSAt4vt1elYkuJsxyGt3byRyBOX_ZAumVgXT_8d9eRlNgwCHsel2JgIcTbBsCYAV7TIdgMvbxDYyt3wMWVkvxGZl_Po7YgkQhbqDcVSVOenHG79PC_8twS60P"
# # # other_info = "https://oauth.vk.com/blank.html#access_token=vk1.a.CoZIh70v9fLG-X83dPlPW8wzpdrfJi30C3t5k1seOVx0CLCN5RBUWEbvqk_XvfVwaVx4g4MnSAt4vt1elYkuJsxyGt3byRyBOX_ZAumVgXT_8d9eRlNgwCHsel2JgIcTbBsCYAV7TIdgMvbxDYyt3wMWVkvxGZl_Po7YgkQhbqDcVSVOenHG79PC_8twS60P&expires_in=0&user_id=720113&state=123456"
#
# fb_tkn = "EAAIoYCOxuPsBAI0FZCreCfCbCVna6aNaJbolvgDr4eZAV8kCrtrIGKnKMjZARTeTzqCMJTglfuWnxcYfjxA8EvFAsLGepUu0ZBvvnZBn5v13C9zZAIVIHMnLzq6872eqBNcMj1zqkGXaXBZBpz7BESeTHjdLP3X3IVg5dkS6gqzezdUxxo94MzbNer3CUxZA2DEZD"
# tkn = "vk1.a.89PP0s0GGvlMEdnz4nkMv0Cj_J91ORTS9VLL-XLblaASL2kcNpywHSKCdCNwAvfbXZVuhFUx-4dO3rutN-WUWz9Zh5zpBXlx6ouFPhrNi5TU469EkrbcqbJgY6K7iub272PillJI2idERmUGozaiVNA5tY5N7fmYZ3IjjplY2lwXSVFXYtkgeEDjXhEZv_mK"
#
session = vk_api.VkApi(token=config.vk_tkn)
vk = session.get_api()
#
#
# def my_id():
#     my_id = vk.account.getProfileInfo()
#     return my_id["id"]
#
# def get_user_status(user_id):
#     status = session.method("status.get", {"user_id": user_id})
#     if status['text'] == '':
#         print("None status((")
#     else:
#         print(status['text'])
#
#
# def set_user_status(prom):
#     # for i in range(1, 30, 1):
#     vk.status.set(text = str(prom))
#         # get_user_status(139882657)
#         # time.sleep(1)
#
#
# def get_chat_info(id):
#     gum = vk.messages.getChat(chat_id=id)
#     # print(gum)
#     for i in gum:
#         print(f"{i}: {gum.get(i)}")
#
# def get_names_chst_users(id):
#     gum = vk.messages.getChat(chat_id=id)
#     id_users = gum["users"]
#     print(id_users)
#     usrs = vk.users.get(user_ids=id_users)
#     for i in range(len(usrs)):
#         print(usrs[i]['first_name'], usrs[i]['last_name'])
#
#
# def get_user_chats():
#     chats = vk.messages.getConversations()
#     print(chats["items"][5]['conversation']['peer'])
#
#
# def get_user_info(id):
#     user_info = vk.users.get(user_ids=id, fields="bdate")
#     name = user_info[0]['first_name']
#     l_name = user_info[0]['last_name']
#     full_name = name + ' ' + l_name
#     return full_name, user_info
#
#
# def search_info(q, lim):
#     result = vk.search.getHints(q=q, limit=lim)
#     # ids = result['items'][0]['profile']['id']
#
#     return result
#
#
# var = int(input(f"Твой id: {my_id()}\n"
#                 "exit - 0\n"
#                 "get_user_status - 1\n"
#                 "set_user_status - 2\n"
#                 "get_chat_info - 3\n"
#                 "get_names_chst_users - 4\n"
#                 "get_user_chats - 5\n"
#                 "get_user_info - 6\n"
#                 "search_info - 7\n"
#                 "Выбор: "))
# a = 1
# while a == 1:
#     if var == 0:
#         break
#     elif var == 1:
#         user_id = input("Введите id: ")
#         get_user_status(user_id)
#         var = int(input("->> "))
#
#     elif var == 2:
#         stat = input("Введите статус: ")
#         set_user_status(stat)
#         var = int(input("->> "))
#
#     elif var == 3:
#         chat = input("Введите id чата: ")
#         get_chat_info(chat)
#         var = int(input("->> "))
#
#     elif var == 4:
#         chat = input("Введите id чата: ")
#         get_names_chst_users(chat)
#         var = int(input("->> "))
#
#     elif var == 5:
#         get_user_chats()
#         var = int(input("->> "))
#
#     elif var == 6:
#         user_id = input("Введите id: ")
#         print(get_user_info(user_id))
#         var = int(input("->> "))
#
#     elif var == 7:
#         quest = input("Введите запрос: ")
#         limit = int(input("Лимит результатов: "))
#         print(search_info(quest, limit))
#         var = int(input("->> "))
#
#
# # set_user_status()
# # get_user_status(139882657)
# # get_user_message(525)
# # get_names_chst_users(525)


# with open('data/id_subs.txt', 'r') as f:
#     for i in f:
#         user = vk.users.get(user_ids=int(i), fields='counters')
#         uuser = user[0]["counters"]["friends"]
#         print(user[0])


# print("Title".center(10, "~"))


# code_to_test = """
# a = 2 * 2
# print(a)
# """
# elapsed_time = timeit.timeit(code_to_test)
# print(f"\n", elapsed_time/524261)

# max_friends = {}
# max_friends[140574805] = 9652
# for s in max_friends.keys():
#     print(s, max_friends[s])

# import sqlite3
# from sqlite3 import Error
#
# def sql_connection():
#     try:
#
#         con = sqlite3.connect('data/main.db')
#         print("Connection done!")
#
#         return con
#
#     except Error:
#
#         print(Error)
#
#
# def sql_table(con):
#
#     cursorObj = con.cursor()
#
#     cursorObj.execute("""CREATE TABLE employees(id integer PRIMARY KEY,
#                                                 name text,
#                                                 salary real,
#                                                 department text,
#                                                 position text,
#                                                 hireDate text
# )""")
#
#     con.commit()
#
# con = sql_connection()
# sql_table(con)

# import sqlite3
# from sqlite3 import Error
#
# def sql_connection():
#     try:
#         con = sqlite3.connect('data/main.db')
#         return con
#     except Error:
#         print(Error)
#
# con = sql_connection()
# c = con.cursor()
# c.execute("""SELECT * FROM sqlite_master WHERE TYPE = 'table'
# """)
# tab = c.fetchall()
# all_tab = []
# for table in tab:
#     all_tab.append(table[1])
#
# if '213135123' in all_tab:
#     print('dawdawda')
# else:
#     print('0000', str(1241312), 'dag2')


# con = sql_connection()
# cur = con.cursor()
#
# cur.execute(f"""SELECT ROWID, user_id, name , lname, count_friends FROM f139882657 WHERE count_friends > 295 ORDER BY count_friends DESC""")
# tabs = cur.fetchall()
# # all_tabs = []
# # for tab in tabs:
# #     all_tabs.append(tab[0])
# print(len(tabs))


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
        return summs * 5
    elif len(score_mass) == 3 and summs == 8:
        return summs * 4
    elif len(score_mass) == 3 and summs == 7:
        return summs * 3
    elif len(score_mass) == 3 and summs == 6:
        return summs * 2

    elif len(score_mass) == 2 and summs == 8 or summs == 9:
        return summs * 6
    elif len(score_mass) == 2 and summs == 6 or summs == 7:
        return summs * 4
    elif len(score_mass) == 2 and summs == 4 or summs == 5:
        return summs * 2

    elif len(score_mass) == 1 and summs == 8 or summs == 9:
        return summs * 10
    elif len(score_mass) == 1 and summs == 6 or summs == 7:
        return summs * 6
    elif len(score_mass) == 1 and summs == 4 or summs == 5:
        return summs * 4
    elif len(score_mass) == 1 and summs == 2 or summs == 3:
        return summs
    else:
        return 0


def check_short(id):
    if len(str(id)) <= 5:
        return 90
    elif len(str(id)) <= 4:
        return 110
    elif len(str(id)) <= 3:
        return 150
    elif len(str(id)) <= 2:
        return 190
    else:
        return 0

id = 666655555
print(check_short(id) + check_polindrom(id) + check_repeat_digits(id))
