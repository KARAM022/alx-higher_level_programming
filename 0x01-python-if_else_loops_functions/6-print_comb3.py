#!/usr/bin/python3
for f in range(10):
    for l in range(f + 1, 10):
        if (f != 8):
            print("{:d}{:d}".format(f, l), end=", ")
        else:
            print("{:d}{:d}".format(f, l), end="\n")
