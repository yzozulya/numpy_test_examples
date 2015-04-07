from numpy import *

a = array([1, 2])
b = array([3, 4])
c = array([5, 6])
column_stack((a, b, c))  # a,b,c are 1-d arrays with equal length
