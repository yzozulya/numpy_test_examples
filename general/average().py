from numpy import *

a = array([1, 2, 3, 4, 5])
w = array([0.1, 0.2, 0.5, 0.2, 0.2])  # weights, not necessarily normalized
average(a)  # plain mean value
average(a, weights=w)  # weighted average
average(a, weights=w, returned=True)  # output = weighted average, sum of weights
