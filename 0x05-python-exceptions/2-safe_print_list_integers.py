#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        if x > 0:
            for i in range(x):
                print("{:d}".format(my_list[i]), end="")
            print()
            return i + 1
        else:
            print()
            return 0
    except (ValueError, TypeError):
        continue
