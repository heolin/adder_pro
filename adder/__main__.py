from __future__ import print_function
import argparse

from lib import add


def main():
    input_parser = argparse.ArgumentParser()
    input_parser.add_argument(
        '-a', '--first', help="First value to add.", required=True)
    input_parser.add_argument(
        '-b', '--second', help="Second value to add.", required=True)
    input_parser.add_argument(
        '-f', '--float', action="store_true",
        help="Add variables with floating precision.")
    args = input_parser.parse_args()

    x = int
    if args.float:
        x = float

    a = x(args.first)
    b = x(args.second)
    print(x(add(a, b)))


if __name__ == "__main__":
    main()
