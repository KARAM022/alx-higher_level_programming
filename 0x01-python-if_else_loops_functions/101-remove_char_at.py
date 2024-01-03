#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    for i in str:
        if (i != str[n:n+1]):
            strcpy += i
    return (strcpy)
