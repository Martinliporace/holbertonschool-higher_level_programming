#!/usr/bin/python3

def rotate_left_list(my_list=[], number_rotation=0):

    new_list = []
    rot = number_rotation
    aux = []

    if(number_rotation > len(my_list)):
        rot = number_rotation - len(my_list)

    for i in range(len(my_list)):
        if i < rot:
            aux.append(my_list[i])
    for j in range(rot, len(my_list)):
        new_list.append(my_list[j])
    for k in aux:
        new_list.append(k)

    return(new_list)
