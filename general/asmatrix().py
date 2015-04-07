from numpy import *

a = array([[1, 2], [5, 8]])
a
m = asmatrix(a)  # m is matrix type with same contents as a -- data is not copied
m
a[0, 0] = -99
a
m  # no copy was made so modifying a modifies m, and vice versa
