#!/usr/bin/python3

def error(av):
    if len(av) is not 8:
        return (84)

    i =	0
    for i in av:
        if i.isnumeric() is False and i[0] is not '-':
            return (84)

    if int(av[0]) < 1 or int(av[0]) > 3 or int(av[7]) < 0:
        return (84)

    for i, j in enumerate(av):
        if i is not 0:
            av[i] = int(j)
    return (0)
