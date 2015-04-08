import numpy.ma as ma

x = ma.masked_equal([0, 1, 0, 2, 3], 0)
x
ma.is_masked(x)
x = ma.masked_equal([0, 1, 0, 2, 3], 42)
x
ma.is_masked(x)
x = [False, True, False]
ma.is_masked(x)
x = 'a string'
ma.is_masked(x)
