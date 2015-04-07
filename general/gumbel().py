from numpy.random import *

gumbel(loc=0.0, scale=1.0, size=(2, 3))  # Gumbel distribution location=0.0, scale=1.0
from pylab import *  # histogram plot example

hist(gumbel(0, 1, (1000)), 50)
