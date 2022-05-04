#!/usr/bin/python3
def uniq_add(my_list=[]):

    aux = []
    res = 0
    for i in my_list:
        if i not in aux:
            aux.append(i)
    for j in aux:
        res += j
    return(res)
