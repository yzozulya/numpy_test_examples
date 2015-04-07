from numpy import *

m = matrix('1 2; 5 8')
m
a = asarray(m)  # a is array type with same contents as m -- data is not copied
a
m[0, 0] = -99
m
a  # no copy was made, so modifying m modifies a, and vice versa
