# import time
# import telebot
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


with open('data/id_subs.txt', 'r') as f:
    for i in f:
        user = vk.users.get(user_ids=int(i), fields='counters')
        uuser = user[0]["counters"]["friends"]
        print(user[0])