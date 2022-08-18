import vk_api
import config

session = vk_api.VkApi(token=config.vk_tkn)
vk = session.get_api()


def my_id():
    my_id = vk.account.getProfileInfo()
    return my_id["id"]


def most_friendly_hmy(id):
    list_friends = vk.friends.get(user_id=id)
    clear_list_friends = list_friends['items']
    print(list_friends['count'], clear_list_friends)


def get_subs_id(id):
    with open('data/id_subs.txt', 'a') as f:
        count_subs = vk.users.getFollowers(user_id=id)
        iter = 0
        count = 0

        while count <= count_subs['count']:
            list_subs = vk.users.getFollowers(user_id=id, offset=iter, count=1000)
            list_id_subs = list_subs['items']

            if count_subs['count'] >= 1000:
                for i in range(1000):
                    id_user = str(list_id_subs[i])
                    f.writelines(id_user + "\n")
                    count += 1
                    print("1- ", count)

            elif count_subs['count'] < 1000:
                for i in range(count_subs['count']):
                    id_user = str(list_id_subs[i])
                    f.writelines(id_user + "\n")
                    count += 1
                    print("2- ", count)

            iter += 1000


def name_with_id_users():
    with open('data/id_subs.txt', 'r') as f:
        for i in f:
            user = vk.users.get(user_ids=i)
            name = user[0]['first_name']
            lname = user[0]['last_name']
            print(f"{name} {lname}")


def more_all_friends():
    with open('data/id_subs.txt', 'r') as f:
        num_1 = 0
        counter = 0
        max_friends = {}
        for i in f:
            user = vk.users.get(user_ids=int(i), fields='counters')
            uuser = user[0]
            if 'counters' in uuser:
                if counter < uuser['counters']['friends']:
                    counter = uuser['counters']['friends']
                    max_friends.clear()
                    max_friends[uuser['id']] = counter
                    print(max_friends)
                    num_1 += 1
        print(max_friends)


more_all_friends()

# get_subs_id(139882657)
