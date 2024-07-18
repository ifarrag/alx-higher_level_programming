#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value += 0
        return True
    except ValueError:
        return False
