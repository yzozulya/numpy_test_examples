s = slice(3, 9, 2)  # slice objects exist outside numpy
from numpy import *

a = arange(20)
a[s]
a[3:9:2]  # same thing
