#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tf_list = []
    if len(my_list) == 0:
        return 0
    else:
        for i in my_list:
            if i % 2 == 0:
                tf_list.append(True)
            else:
                tf_list.append(False)
        return tf_list
