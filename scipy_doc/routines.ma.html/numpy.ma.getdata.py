import numpy.ma as ma

a = ma.masked_equal([[1, 2], [3, 4]], 2)
a
ma.getdata(a)
a.data
