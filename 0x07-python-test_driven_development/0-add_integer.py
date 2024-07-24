#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is float:
        a = int(a)
    elif type(a) is not int:
        raise ValueError("a must be an integer")
    if type(b) is float:
        b = int(b)
    elif type(b) is not int:
        raise ValueError("b must be an integer")

    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testfile()
