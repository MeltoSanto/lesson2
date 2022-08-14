import vk_api
import config

session = vk_api.VkApi(token=config.vk_tkn)
vk = session.get_api()

def my_id():
    my_id = vk.account.getProfileInfo()
    return my_id["id"]


def most_friendly_homy(id):
    list_friends = vk.friends.get(user_id=id)
    clear_list_friends = list_friends['items']
    print(list_friends['count'], clear_list_friends)


def stat_subs(id):
    with open('data/id_subs.txt', 'w+') as f:
        count_subs = vk.users.getFollowers(user_id=id)
        iter = 0
        count = 0
        while iter < int(count_subs['count']):
            if count < int(count_subs['count']):
                list_subs = vk.users.getFollowers(user_id=id, offset=iter, count=1000)
                list_id_subs = list_subs['items']
                for i in range(0, 999, 1):
                    f.writelines(str(list_id_subs[i]) + "\n")
                    count += 1
                    # list.append(list_subs['items'][i])
            else:
                for line in f.readlines():
                    user_info = vk.users.get(user_ids=line)
                    name = user_info[0]['first_name']
                    l_name = user_info[0]['last_name']
                    full_name = name + ' ' + l_name
                    print(line)
            iter += 1000
        print(123)

# most_friendly_homy(38232403)
stat_subs(170126572)