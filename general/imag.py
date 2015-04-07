from numpy import *

a = array([1 + 2j, 3 + 4j, 5 + 6j])
a.imag
a.imag = 9
a
a.imag = array([9, 8, 7])
a
