#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv
    cant = len(args)

    res = 0

    if cant != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = args[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(args[1])
    b = int(args[3])

    if args[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif args[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif args[2] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
