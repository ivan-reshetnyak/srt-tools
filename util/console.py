import sys
from .FatalError import FatalError


def parse():
    res = dict()
    for arg in sys.argv[1:]:
        try:
            key, value = arg.split("=")
            res[key] = value
        except ValueError:
            print("Wrong argument format: %s, must be <key>=<value>" % arg)

    return res
