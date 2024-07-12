#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    special = []
    for i in set(set_1):
        x = 0
        for n in set(set_2):
            if n == i:
                x = 1
        if x == 0:
            special.append(n)
    for a in set(set_2):
        x = 0
        for b in set(set_1):
            if b == a:
                x = 1
        if x == 0:
            special.append(b)
    return set(special)
