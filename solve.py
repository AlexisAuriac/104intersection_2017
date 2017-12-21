#!/usr/bin/python3

import utilities

def put_points(sol, p, v):
    for i in sol:
        x = float(p[0]) + i * float(v[0])
        y = float(p[1]) + i * float(v[1])
        z = float(p[2]) + i * float(v[2])
        x = utilities.set_prec(x, 3)
        y = utilities.set_prec(y, 3)
        z = utilities.set_prec(z, 3)
        print("({0},{1},{2})".format(x, y, z))
        
def cylindre(av):
    a = int(av[4])**2 + int(av[5])**2
    b = 2*int(av[1])*int(av[4]) + 2*int(av[2])*int(av[5])
    c = int(av[1])**2 + int(av[2])**2 - int(av[7])**2
    sol = utilities.secdegree(a, b, c)
    if sol == -1:
        print("There is an infinite number of intersection points.")
        return (0)
    if len(sol) is 0:
        print("No intersection point.")
    elif len(sol) is 1:
        print("1 intersection point :")
    else:
        print("2 intersection points :")
    put_points(sol, av[1:4], av[4:7])
