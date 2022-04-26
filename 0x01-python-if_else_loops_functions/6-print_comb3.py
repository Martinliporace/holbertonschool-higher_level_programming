#!/usr/bin/python3
for dec in range(0, 9):
    for uni in range(0, 10):
        if uni > dec and dec != 8:
            print("{:}".format(dec)+"{:}".format(uni), end=', ')
        elif uni > dec and dec == 8:
            print("{:}".format(89), end='\n')
