from numpy import *

a = array([1, 2, 2, 3])  # a is 1-D and in ascending order.
a.searchsorted(2)  # side defaults to "left"
a.searchsorted(2, side='right')  # look for the other end of the run of twos
a.searchsorted(4)  # 4 is greater than any element in a
a.searchsorted([[1, 2], [2, 3]])  # whoa, fancy keys
searchsorted(a, 2)  # there is a functional form
