from numpy import *

a = array([True, False, True])
a.all()  # if all elements of a are True: return True; otherwise False
all(a)  # this form also exists
a = array([1, 2, 3])
all(a > 0)  # equivalent to (a > 0).all()
