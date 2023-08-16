#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sumup = 0
    mid = 0

    for idx in my_list:
        sumup += idx[0] * idx[1]
        mid += idx[1]
    avrg = sumup / mid
    return avrg
