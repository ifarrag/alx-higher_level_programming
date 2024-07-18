#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if x > 0:
        divide = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except (ValueError, TypeError):
                divide = divide + 1
                continue
        print()
        return i + 1 - divide
    else:
        print()
        return 0
