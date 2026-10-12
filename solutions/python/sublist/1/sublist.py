"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if in_list(list_one, list_two):
        return SUBLIST
    if in_list(list_two, list_one):
        return SUPERLIST
    return UNEQUAL

def in_list(small_list, large_list):
    if not small_list:
        return True
    l_len, s_len = len(large_list), len(small_list)
    for i in range(l_len - s_len + 1):
        if large_list[i:i + s_len] == small_list:
            return True
    return False
