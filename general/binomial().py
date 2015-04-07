from numpy.random import *

binomial(n=100, p=0.5, size=(2, 3))  # binomial distribution n trials, p= success probability
from pylab import *  # histogram plot example

hist(binomial(100, 0.5, (1000)), 20)
