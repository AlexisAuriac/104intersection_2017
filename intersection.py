#!/usr/bin/python3

import sys
import error
import show

if __name__ == "__main__":
    av = sys.argv[1:]
    if error.error(av) is 84:
        exit(84)
    show.type(av)
    show.line(av)
