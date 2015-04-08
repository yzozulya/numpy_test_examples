import numpy.ma as ma

a = ma.arange(3)
a[1] = ma.masked
b = ma.arange(2, 5)
a
b
ma.concatenate([a, b])
