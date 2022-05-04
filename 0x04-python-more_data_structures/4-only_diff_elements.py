#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    set_3 = set()
    for i in set_1:
        if i not in set_2:
            set_3.add(i)
    for j in set_2:
        if j not in set_1:
            set_3.add(j)

    return(set_3)
