#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x > 0:
            for i in range(x):
                print("{}".format(my_list[i]), end="")
            print()
            return i+1
        else:
            print()
            return 0
    except IndexError:
        print()
        return i
