#!/usr/bin/python3
def uppercase(str):
    for c in str:
        av = ord(c)
        if 97 <= av <= 122:
            upp = chr(av - 32)
        else:
            upp = c
        print("{}".format(upp), end="")
    print()

