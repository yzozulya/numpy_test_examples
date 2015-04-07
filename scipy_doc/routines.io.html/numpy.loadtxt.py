import numpy as np
from StringIO import StringIO  # StringIO behaves like a file object

c = StringIO("0 1\n2 3")
np.loadtxt(c)
d = StringIO("M 21 72\nF 35 58")
np.loadtxt(d, dtype={'names': ('gender', 'age', 'weight'),
                     'formats': ('S1', 'i4', 'f4')})
c = StringIO("1,0,2\n3,0,4")
x, y = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True)
x
y
