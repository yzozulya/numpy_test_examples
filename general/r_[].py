from numpy import *

r_[1:5]  # same as arange(1,5)
r_[1:10:4]  # same as arange(1,10,4)
r_[1:10:4j]  # same as linspace(1,10,4), 4 equally-spaced elements between 1 and 10 inclusive
r_[1:5, 7, 1:10:4]  # sequences separated with commas are concatenated
r_['r', 1:3]  # return a matrix. If 1-d, result is a 1xN matrix
r_['c', 1:3]  # return a matrix. If 1-d, result is a Nx1 matrix
a = array([[1, 2, 3], [4, 5, 6]])
r_[a, a]  # concatenation along 1st (default) axis (row-wise, that's why it's called r_)
r_['-1', a, a]  # concatenation along last axis, same as c_[a,a]
