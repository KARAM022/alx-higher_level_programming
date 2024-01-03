#!/usr/bin/python3
def remove_char_at(str, n):
    if (n >= 0):
        strcpy = ""
        for i in str:
            if (i != str[n:n+1]):
                strcpy += i
        return (strcpy)
    else:
        return (str)
