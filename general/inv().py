from numpy import *
from numpy.linalg import inv

a = array([[3, 1, 5], [1, 0, 8], [2, 1, 4]])
print a
inva = inv(a)  # Inverse matrix
print inva
dot(a, inva)  # Check the result, should be eye(3) within machine precision
