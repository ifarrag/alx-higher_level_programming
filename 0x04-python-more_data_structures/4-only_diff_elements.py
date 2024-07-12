#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    special = []
    common = []
    for i in set(set_1):
        for n in set(set_2):
            if n != i:
                special.append(n)
    return special
