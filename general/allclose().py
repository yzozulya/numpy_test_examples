from numpy import *

allclose(array([1e10, 1e-7]), array([1.00001e10, 1e-8]))
allclose(array([1e10, 1e-8]), array([1.00001e10, 1e-9]))
allclose(array([1e10, 1e-8]), array([1.0001e10, 1e-9]))
