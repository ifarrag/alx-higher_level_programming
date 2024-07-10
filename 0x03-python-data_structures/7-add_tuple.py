#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_t = []
    for i in range(2):

        if len(tuple_a) == 0 or tuple_a is None:
            a = (0, 0)
        elif i > len(tuple_a):
            a = (0, 0)
        else:
            a = tuple_a
        if len(tuple_b) == 0 or tuple_b is None:
            b = (0, 0)
        elif i > len(tuple_b):
            b = (0, 0)
        else:
            b = tuple_b
        new_t.append(a[i] + b[i])
    return (new_t[0], new_t[1])
