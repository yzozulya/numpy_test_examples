import numpy.ma as ma

a = ma.masked_equal([[1, 2], [3, 4]], 2)
a
ma.getmask(a)
a.mask
b = ma.masked_array([[1, 2], [3, 4]])
b
ma.nomask
ma.getmask(b) == ma.nomask
b.mask == ma.nomask
