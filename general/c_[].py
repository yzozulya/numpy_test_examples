from numpy import *

c_[1:5]  # for single ranges, c_ works like r_
c_[1:5, 2:6]  # for comma separated values, c_ stacks column-wise
a = array([[1, 2, 3], [4, 5, 6]])
c_[a, a]  # concatenation along last (default) axis (column-wise, that's why it's called c_)
c_['0', a, a]  # concatenation along 1st axis, equivalent to r_[a,a]
