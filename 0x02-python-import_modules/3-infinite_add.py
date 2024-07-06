#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    if len(argv) > 1:
        for i in range(1, len(argv)):
            sum = int(argv[i]) + sum
        print("{:d}".format(sum))
    else:
        print("{:d}".format(0))
