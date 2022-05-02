#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    cpa = [0, 0, 0, 0]
    cpb = [0, 0, 0, 0]

    for i in range(len(tuple_a)):
        cpa[i] = tuple_a[i]
    for j in range(len(tuple_b)):
        cpb[j] = tuple_b[j]

    return(cpa[0] + cpb[0], cpa[1] + cpb[1])
