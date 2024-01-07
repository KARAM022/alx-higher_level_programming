#!/usr/bin/python3
new = []
def new_in_list(my_list, idx, element):
    for i in my_list:
        new[i] = my_list[i]
    if (idx >= 0 and idx < len(my_list)):
        new[idx] = element
        return (new)
    else:
        return (new)
    