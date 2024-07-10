#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for i in range(len(my_string)):
        if 'C' not in my_string[i] and 'c' not in my_string[i]:
            string += my_string[i]
    return string
