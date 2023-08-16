#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romans = 0

    for k in range(len(roman_string)):
        if k > 0 and nums[roman_string[k]] > nums[roman_string[k-1]]:
            romans += nums[roman_string[k]] - 2 * nums[roman_string[k-1]]
        else:
            romans += nums[roman_string[k]]

    return romans
