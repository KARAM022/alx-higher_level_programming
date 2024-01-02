#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        if (i < 99):
            if((i % 3 == 0) and (i % 5 != 0)):
                i = "Fizz"
            if((i % 3 != 0) and (i % 5 == 0)):
                i = "Buzz"
            if((i % 3 == 0) and (i % 5 == 0)):
                i = "FizzBuzz"
            print("{:02d}, ".format(i), end="")
        else:
            print("{:02d}".format(i), end="\n")
