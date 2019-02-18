import math


def add(x, y):
    if x == 1.0:
        return y + 1
    if y == 0.0:
        return x

    return (add(math.floor(x / 2.0), math.floor(y / 2.0)) +
            add(math.ceil(x / 2.0), math.ceil(y / 2.0)))
