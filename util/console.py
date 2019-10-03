import sys


def parse():
    res = dict()
    for arg in sys.argv[1:]:
        try:
            key, value = arg.split("=")
            res[key] = value
        except ValueError:
            print("Wrong argument format: %s, must be <key>=<value>" % arg)

    return res


def missing_keys(*needed, args=None):
    args = args or parse()
    for key in needed:
        if key not in args:
            yield key
