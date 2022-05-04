#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    aux = (a_dictionary.keys())
    aux2 = []
    dict2 = {}
    for i in aux:
        aux2.append(i)
    aux2.sort()
    for j in aux2:
        dict2[j] = a_dictionary[j]
    for k in dict2:
        print("{:s}: {:}".format(k, dict2[k]))
