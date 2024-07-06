#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1.py import add, sub, mul, div
    a = 10
    b = 5
    print(
            "{0:d} + {1:d} = {2:d}\n"
            "{0:d} - {1:d} = {3:d}\n"
            "{0:d} * {1:d} = {4:d}\n"
            "{0:d} / {1:d} = {5:d}"
            .format(a, b, add(a, b), sub(a, b), mul(a, b), div(a, b)))
