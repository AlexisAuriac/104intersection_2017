#!/usr/bin/python3

import utilities

def show_float(nb, prec):
    if type(nb) is not float:
        raise TypeError("Argument must be a float")
    nb = str(nb)
    int_part, float_part = nb.split(".")
    print(",".join([int_part, float_part[:prec]]))

def type(surface, param):
    """displays the type and paramter of the object"""
    disp = str()

    if surface is "1":
        surface = "sphere"
        disp = "radius " + str(param)
    elif surface is "2":
        surface = "cylinder"
        disp = "radius " + str(param)
    else:
        surface = "cone"
        disp = str(param) + " degree angle"
    print(surface, "of", disp)
    return (surface)

def line(p, v):
    """displays infos about the line"""
    print("straight line going through the ({0},{1},{2})"\
          .format(p[0], p[1], p[2]), end=' ')
    print("point and of direction vector ({0},{1},{2})"\
          .format(v[0], v[1], v[2]))

def nb_sol(sol):
    if len(sol) is 0:
        print("No intersection point.")
    elif len(sol) is 1:
        print("1 intersection point :")
    else:
        print("2 intersection points :")
    return (1)

def points(sol, p, v):
    for i in sol:
        x = float(p[0]) + i * float(v[0])
        y = float(p[1]) + i * float(v[1])
        z = float(p[2]) + i * float(v[2])
        print("(%.3f, %.3f, %.3f)" % (x, y, z))
