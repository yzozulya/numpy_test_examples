from numpy import *

a = array([10, 20, 30, 40])
condition = (a > 15) & (a < 35)
condition
a.compress(condition)
a[condition]  # same effect
compress(a >= 30, a)  # this form also exists
b = array([[10, 20, 30], [40, 50, 60]])
b.compress(b.ravel() >= 22)
x = array([3, 1, 2])
y = array([50, 101])
b.compress(x >= 2, axis=1)  # illustrates the use of the axis keyword
b.compress(y >= 100, axis=0)
