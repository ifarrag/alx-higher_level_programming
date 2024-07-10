#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if 'C' or 'c' in my_string[i]:
            del my_string[i]
    return my_string
