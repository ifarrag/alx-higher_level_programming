#!/usr/bin/python3
def best_score(a_dictionary):
    new_l = []
    biggi = 0
    if a_dictionary is None:
        return None
    for i, y in a_dictionary.items():
        new_l.append(y)
    new_l = sorted(new_l)
    biggi = new_l[-1]
    for i, y in a_dictionary.items():
        if biggi == y:
            return i

