#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:
        return('None')
    aux = list(a_dictionary.values())
    res = 0
    for i in aux:
        if i > res:
            res = i
    for key, value in a_dictionary.items():
        if res == value:
            return(key)
