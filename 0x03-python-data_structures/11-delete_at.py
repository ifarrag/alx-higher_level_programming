#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    else:
        for i in range(len(my_list)):
            if i == idx:
                my_list[i:i+1] = []
                return my_list
        return my_list
