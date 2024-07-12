#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    special = []
    common = []
    for i in set(set_1):
        for n in set(set_2):
            if n != i:
                special.append(n)
            else:
                common.append(n)
    for y in set(set_1):
        i = 0
        for x in common:
            if x == y:
                i = 1
        if i == 0:
            special.append(y)
    return set(special)
