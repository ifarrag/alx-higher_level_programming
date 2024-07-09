#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return "None"
    else:
        for i in my_list:
            if i == idx:
                print("Element at index {:d} is {:d}".format(i, my_list[i]))
        if i < idx:
            return "None"
