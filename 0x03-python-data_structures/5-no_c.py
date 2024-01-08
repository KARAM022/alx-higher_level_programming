#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None
    strnew = ""
    for i in my_string:
        if i != "c" and i != "C":
            strnew += i
    return(strnew)
