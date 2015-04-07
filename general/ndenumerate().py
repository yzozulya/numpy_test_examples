from numpy import *

a = arange(9).reshape(3, 3) + 10
a
b = ndenumerate(a)
for position, value in b:
    print position, value  # position is the N-dimensional index
