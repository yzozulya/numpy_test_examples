from numpy import *

a = arange(10, 100, 10).reshape(3, 3)
a
triu(a, k=0)
triu(a, k=1)
