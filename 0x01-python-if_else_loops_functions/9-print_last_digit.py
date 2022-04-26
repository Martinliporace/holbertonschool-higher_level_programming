#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastDig = number % -10 * -1

    else:
        lastDig = number % 10
    print("{:d}".format(lastDig), end='')
    return (lastDig)
