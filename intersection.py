#!/usr/bin/python3

import sys
from math import *
import error
import solve
import show

if __name__ == "__main__":
    av = sys.argv[1:]
    if error.error(av) is 84:
        exit(84)
    show.type(av)
    show.line(av)
    if av[0] is "sphere":
        solve.sphere(av)
    elif av[0] is "cylinder":
        solve.cylindre(av)
