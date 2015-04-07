from numpy import *


def myfunc(x):
    if x >= 0:
        return x ** 2
    else:
        return -x

myfunc(2.)  # works fine
myfunc(array([-2, 2]))  # doesn't work, try it...
vecfunc = vectorize(myfunc, otypes=[float])  # declare the return type as float
vecfunc(array([-2, 2]))  # works fine!
