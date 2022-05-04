#!/usr/bin/python3
def search_replace(my_list, search, replace):

    aux = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            aux[i] = replace
    return(aux)
