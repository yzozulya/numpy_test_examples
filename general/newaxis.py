from numpy import *

x = arange(3)
x
x[:, newaxis]  # add a new dimension/axis
x[:, newaxis, newaxis]  # add two new dimensions/axes
x[:, newaxis] * x
y = arange(3, 6)
x[:, newaxis] * y  # outer product, same as outer(x,y)
x.shape
x[newaxis, :].shape  # x[newaxis,:] is equivalent to x[newaxis] and x[None]
x[:, newaxis].shape
