#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):

    """chequear si key existe y comparar value en caso positivo"""
    if key in a_dictionary and a_dictionary[key] != value:
        """si existe y cambia el valor, actualizarlo"""
        a_dictionary[key] = value

    """si no existe key, agregarla"""

    a_dictionary[key] = value
    return(a_dictionary)
