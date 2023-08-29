#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    sumup = 0
    for elem in range(x):
        try:
            print(my_list[elem], end="")
            sumup += 1
        except IndexError:
            break
    print()
    return sumup
