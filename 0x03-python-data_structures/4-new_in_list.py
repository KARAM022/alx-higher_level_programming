#!/usr/bin/python3
new = []
def new_in_list(my_list, idx, element):
    for i in range(0,len(my_list)):
        # new[i] = my_list[i]
        print(new[0])
    if (idx >= 0 and idx < len(my_list)):
        new[idx] = element
        return (new)
    else:
        return (new)
print(new_in_list([1,2,3], 1, 1))