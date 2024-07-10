#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_t = []
    for i in range(2):
        if len(tuple_a) < i:
            a = (0, 0)
        else:
            a = tuple_a
        if len(tuple_b) < i:
            b = (0, 0)
        else:
            b = tuple_b
        new_t.append(a[i] + b[i])
    return (new_t[0], new_t[1])
