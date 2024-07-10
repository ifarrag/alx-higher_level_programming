#!/usr/bin/python3
def no_c(my_string):
    string = []
    for i in range(len(my_string)):
        if {'c','C'} not in my_string[i]:
            string.append(my_string[i])
    return string
