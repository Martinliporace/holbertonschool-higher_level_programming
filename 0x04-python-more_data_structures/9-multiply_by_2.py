#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    dict2 = {}

    for i in a_dictionary:
        dict2[i] = a_dictionary[i] * 2
    return(dict2)
