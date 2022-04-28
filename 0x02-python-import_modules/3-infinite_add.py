#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv

    cant = len(args)
    cont = 1
    res = 0

    for i in range(1, cant):
        res += int(args[i])
        cont += 1
    print(res)
