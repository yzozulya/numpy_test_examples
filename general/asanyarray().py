from numpy import *

a = array([[1, 2], [5, 8]])
a
m = matrix('1 2; 5 8')
m
asanyarray(a)  # the array a is returned unmodified
asanyarray(m)  # the matrix m is returned unmodified
asanyarray([1, 2, 3])  # a new array is constructed from the list
