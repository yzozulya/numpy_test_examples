from numpy import *

a = arange(10, 100, 10).reshape(3, 3)
a
tril(a, k=0)
tril(a, k=1)
