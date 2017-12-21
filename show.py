#!/usr/bin/python3

def show_float(nb, prec):
    if type(nb) is not float:
        raise TypeError("Argument must be a float")
    nb = str(nb)
    int_part, float_part = nb.split(".")
    print(",".join([int_part, float_part[:prec]]))

def type(av):
    """displays the type and paramter of the object"""
    if av[0] is "1":
        av[0] = "sphere"
        av[7] = "radius " + av[7]
    elif av[0] is "2":
        av[0] = "cylinder"
        av[7] = "radius " + av[7]
    else:
        av[0] = "cone"
        av[7] = av[7] + " degree angle"
    print(av[0], "of", av[7])
    av[7] = av[7].split(" ")
    for i in av[7]:
        if i.isnumeric() == True:
            av[7] = i

def line(av):
    """displays infos about the line"""
    str = "straight line going through the ({0},{1},{2})"\
          .format(av[1], av[2], av[3])
    str += " point and of direction vector ({0},{1},{2})"\
           .format(av[4], av[5], av[6])
    print(str)
