#!/usr/bin/python3

import sys
from math import *
import error
import solve
import show

def main(av):
    if error.error(av) is 84:
        exit(84)
    av[0] = show.type(av[0], av[7])
    show.line(av[1:4], av[4:7])
    if av[0] is "sphere":
        solve.sphere(av[1:4], av[4:7], av[7])
    elif av[0] is "cylinder":
        solve.cylindre(av[1:4], av[4:7], av[7])
    elif av[0] is "cone":
        solve.cone(av[1:4], av[4:7], av[7])
    exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])
