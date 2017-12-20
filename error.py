#!/usr/bin/python3

def error(av):
    if len(av) is not 8:
        return (84)

    i =	0
    for i in av:
        if i.isnumeric() is False:
            return (84)

    if int(av[0]) < 1 or int(av[0]) > 3 or int(av[7]) < 0:
        return (84)
    return (0)
