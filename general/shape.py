from numpy import *

x = arange(12)
x.shape
x.shape = (3, 4)  # array with 3 rows and 4 columns. 3x4=12. Total number of elements is always the same.
x
x.shape = (3, 2, 2)  # 3x2x2 array; 3x2x2 = 12. x itself _does_ change, unlike reshape().
x
x.shape = (2, -1)  # 'missing' -1 value n is calculated so that 2xn=12, so n=6
x
x.shape = 12  # x.shape = (1,12) is not the same as x.shape = 12
x
