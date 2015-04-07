from numpy import *

x = array([0, 0, 0, 1, 2, 3, 0, 0])
trim_zeros(x, 'f')  # remove zeros at the front
trim_zeros(x, 'b')  # remove zeros at the back
trim_zeros(x, 'bf')  # remove zeros at the back and the front
