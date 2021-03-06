#!/usr/bin/python3
def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return(0)
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    aux = []

    for i in roman_string:
        if i in values:
            aux.append(values[i])

    aux.append(0)
    validos = [1, 10, 100]
    res = 0
    for j in range(0, len(aux) - 1):

        if aux[j + 1] > aux[j] and aux[j] in validos:
            res = res - aux[j]

        else:
            res += aux[j]
    return(res)
