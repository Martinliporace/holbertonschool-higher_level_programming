#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv

    cant = len(args)

    if cant == 1:
        print(cant - 1, "arguments.")
    elif cant == 2:
        print(cant - 1, "argument:\n1:", args[1])

    else:
        print(cant - 1, "arguments:")
        cont = 1
        for i in range(1, cant):
            print(cont, ":", args[i])
            cont += 1
