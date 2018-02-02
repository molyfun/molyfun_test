#!usr/bin/python
#-*- coding:utf8 -*-

import re
import random
from datetime import datetime, timedelta, date
from utils.area_dict import area_dict

id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]


def is_id_card(id_number):
    if len(id_number) != 18:
        return False, "Length error"
    if not re.match(r"^\d{17}(\d|X|x)$", id_number):
        return False, "Format error"
    if id_number[0:6] not in area_dict:
        return False, "Area code error"
    try:
        date(int(id_number[6:10]), int(id_number[10:12]), int(id_number[12:14]))
    except ValueError as ve:
        return False, "Datetime error: {0}".format(ve)
    if str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in id_number[0:-1]])]) % 11]) != \
            str(id_number.upper()[-1]):
        return False, "Check code error"
    return True, "{}省 {}市 {}".format(area_dict[id_number[0:2] + "0000"].rstrip("省"),
                                     area_dict[id_number[0:4] + "00"].rstrip("市"),
                                     area_dict[id_number[0:6]])


def gen_id_card(area_code, age, gender):
    if str(area_code) not in area_dict.keys():
        return None
    datestring = str(date(date.today().year - age, 1, 1) + timedelta(days=random.randint(0, 364))).replace("-", "")
    rd = random.randint(0, 999)
    if gender == 0:
        gender_num = rd if rd % 2 == 0 else rd + 1
    else:
        gender_num = rd if rd % 2 == 1 else rd - 1
    result = str(area_code) + datestring + str(gender_num).zfill(3)
    return result + str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in result])]) % 11])


def gen_id_card_random():
    area_code_list = list(area_dict.keys())
    index =  random.randint(0, area_code_list.__len__())
    area_code = area_code_list.__getitem__(index)
    age = random.randint(20, 60)
    gender =  random.randint(0, 1)
    return gen_id_card(int(area_code),age, gender)


if __name__ == "__main__":
    """
    area_code = random.choice(["420102", "420103", "420104", "420105", "420106", "420107"])
    id_number = gen_id_card(int(area_code), 22, 1)
    print(id_number)
    print(is_id_card(id_number))
    """
    print(gen_id_card_random())