#!/usr/bin/python3

import utilities
import show

def sphere(p, v, R):
    a = v[0]**2 + v[1]**2 + v[2]**2
    b = 2*p[0]*v[0] + 2*p[1]*v[1] + 2*p[2]*v[2]
    c = p[0]**2 + p[1]**2 + p[2]**2 - R**2
    sol = utilities.secdegree(a, b, c)

    show.nb_sol(sol)
    show.points(sol, p, v)

def cylindre(p, v, R):
    a = v[0]**2 + v[1]**2
    b = 2*p[0]*v[0] + 2*p[1]*v[1]
    c = p[0]**2 + p[1]**2 - R**2
    sol = utilities.secdegree(a, b, c)
    
    if sol == -1:
        print("There is an infinite number of intersection points.")
        return (0)
    show.sol(sol)
    show.points(sol, p, v)

def cone(p, v, C):
    if c == 90:
        print("bla")
