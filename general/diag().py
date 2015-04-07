from numpy import *

a = arange(12).reshape(4, 3)
print a
print diag(a, k=0)
print diag(a, k=1)
print diag(array([1, 4, 5]), k=0)
print diag(array([1, 4, 5]), k=1)
