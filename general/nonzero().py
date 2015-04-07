from numpy import *

x = array([1, 0, 2, -1, 0, 0, 8])
indices1 = x.nonzero()  # find the indices of the nonzero elements
indices1
x[indices1]
y = array([[0, 1, 0], [2, 0, 3]])
indices = y.nonzero()
print(type(indices))
y[indices[0], indices[1]]  # one way of doing it, explains what's in indices[0] and indices[1]
y[indices]  # this way is shorter
y = array([1, 3, 5, 7])
indices = (y >= 5).nonzero()
y[indices]
nonzero(y)  # function also exists
print y >= 5
print type(y >= 5)
print indices