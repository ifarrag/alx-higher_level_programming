#!/usr/bin/python3
def print_last_digit(number):
    if  number == 0:
        print("{:d}".format(0), end="")
        return 0
    elif number < 0:
        number = -number
        print("{:d}".format(number % 10), end="")
        return number % 10
    else:
        print("{:d}".format(number % 10), end="")
        return number % 10
