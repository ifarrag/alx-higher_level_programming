#!/usr/bin/python3
def uppercase(str):
    listString = []
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            listString.append(chr(ord(i) - 32))
        else:
            listString.append(i)
    for n in range(len(listString)):
        print(listString[n], end="")
    print()
