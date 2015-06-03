#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------

import argparse
import math


def add(x, y):
    if x == 1.0:
        return y + 1
    if y == 0.0:
        return x

    return add(math.floor(x/2.0), math.floor(y/2.0)) + add(math.ceil(x/2.0), math.ceil(y/2.0))

def main():
    input_parser = argparse.ArgumentParser()
    input_parser.add_argument('-a', '--first',  help="First value to add.", required=True)
    input_parser.add_argument('-b', '--second',  help="Second value to add.", required=True)
    input_parser.add_argument('-f', '--float', action="store_true", help="Add variables with floating precision.")
    args = input_parser.parse_args()

    x = int
    if args.float:
        x = float

    a = x(args.first)
    b = x(args.second)
    print x(add(a, b))


if __name__ == "__main__":
    main()
