#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    sum_l = 0
    for i in new_list:
        sum_l += i
    return sum_l
