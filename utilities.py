#!/usr/bin/python3

from math import *

def secdegree(a, b, c):
    delta = b**2 - 4*a*c
    sol = list()

    if a == 0:
        return (-1)
    if delta == 0:
        sol.append(-b/(2*a))
    elif delta > 0:
        sol.append((-b+sqrt(delta))/(2*a))
        sol.append((-b-sqrt(delta))/(2*a))
    return (sol)

def set_prec(float_nb, prec):
    if type(float_nb) is not float:
        raise TypeError("Argument must be a float")
    float_nb = str(float_nb)
    int_part, float_part = float_nb.split(".")
    float_part = float_part[:prec]
    float_nb = int_part + "." + float_part
    i = 0
    while i < prec - len(float_part):
        float_nb += "0"
        i += 1
    return (float_nb)
