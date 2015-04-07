from numpy import *

a = arange(30)
a = a.reshape(2, 3, 5)
a
b = a.transpose()
b
b.shape
b = a.transpose(1, 0, 2)  # First axis 1, then axis 0, then axis 2
b
b.shape
b = transpose(a, (1, 0, 2))  # A separate transpose() function also exists
