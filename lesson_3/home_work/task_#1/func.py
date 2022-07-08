from datetime import date, datetime


def control_real_date(y, m, d):
    try:
        date(y, m, d)
        return True
    except:
        return False

def week_day(y, m, d):
    week_days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    dt = date(y, m, d)
    return week_days[dt.weekday()]


def check_date(str_date):
    str_date_list = str_date.split('.')
    i_d_l = list(map(int, str_date_list))
    if control_real_date(i_d_l[2], i_d_l[1], i_d_l[0]):
        print(f"Дата: {'.'.join(str_date_list)} - существует. Это {week_day(i_d_l[2], i_d_l[1], i_d_l[0])}.")
    else:
        print(f"Дата: {'.'.join(str_date_list)} - не существует.")
