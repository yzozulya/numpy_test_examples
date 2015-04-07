from numpy import *


def myfunc(a):  # function works on a 1d arrays, takes the average of the 1st an last element
    return (a[0] + a[-1]) / 2


b = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
apply_along_axis(myfunc, 0, b)  # apply myfunc to each column (axis=0) of b
apply_along_axis(myfunc, 1, b)  # apply myfunc to each row (axis=1) of b
