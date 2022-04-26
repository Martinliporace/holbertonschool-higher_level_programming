#!/usr/bin/python3
def remove_char_at(str, n):
    copia = ""
    for i in range(len(str)):
        if i != n:
            copia = copia + str[i]
    return(copia)
