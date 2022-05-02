#!/usr/bin/python3
def no_c(my_string):

    cpy = my_string[:]
    chars = "cC"
    cpy = ''.join(x for x in my_string if x not in chars)
    return(cpy)
