from numpy import *

a = array([True, False, True])
a.any()  # gives True if at least 1 element of a is True, otherwise False
any(a)  # this form also exists
a = array([1, 2, 3])
(a >= 1).any()  # equivalent to any(a >= 1)
