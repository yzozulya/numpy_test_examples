from numpy import *

a = array([1 + 2j, 3 + 4j, 5 + 6j])
a.real
a.real = 9
a
a.real = array([9, 8, 7])
a
