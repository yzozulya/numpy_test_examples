import numpy as np
import numpy.ma as ma

a = np.arange(4)
a
ma.masked_where(a <= 2, a)
b = ['a', 'b', 'c', 'd']
ma.masked_where(a == 2, b)
c = ma.masked_where(a <= 2, a)
c
c[0] = 99
c
a
c = ma.masked_where(a <= 2, a, copy=False)
c[0] = 99
c
a
a = np.arange(4)
a = ma.masked_where(a == 2, a)
a
b = np.arange(4)
b = ma.masked_where(b == 0, b)
b
ma.masked_where(a == 3, b)
