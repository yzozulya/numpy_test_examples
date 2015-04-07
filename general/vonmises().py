from numpy.random import *

vonmises(mu=1, kappa=1, size=(2, 3))  # Von Mises distribution mean=1.0, kappa=1
from pylab import *  # histogram plot example

hist(vonmises(1, 1, (10000)), 50)
