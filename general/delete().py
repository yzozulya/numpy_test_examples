from numpy import *

a = array([0, 10, 20, 30, 40])
delete(a, [2, 4])  # remove a[2] and a[4]
a = arange(16).reshape(4, 4)
a
delete(a, s_[1:3], axis=0)  # remove rows 1 and 2
delete(a, s_[1:3], axis=1)  # remove columns 1 and 2
