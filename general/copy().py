from numpy import *

a = array([1, 2, 3])
a
b = a  # b is a reference to a
b[1] = 4
a
a = array([1, 2, 3])
b = a.copy()  # b is now an independent copy of a
b[1] = 4
a
b
