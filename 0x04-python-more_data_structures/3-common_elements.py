#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_l = []
    for i in set(set_1):
        for n in set(set_2):
            if n == i:
                new_l.append(n)
    return new_l
