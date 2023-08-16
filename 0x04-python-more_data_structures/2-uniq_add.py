#!/usr/bin/python3
def uniq_add(my_list=[]):
    mylist = set(my_list)
    sumup = 0
    for num in mylist:
        sumup += num
    return sumup
