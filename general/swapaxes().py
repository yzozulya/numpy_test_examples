from numpy import *

a = arange(30)
a = a.reshape(2, 3, 5)
a
b = a.swapaxes(1, 2)  # swap the 2nd and the 3rd axis
b
b.shape
b[0, 0, 0] = -1  # be aware that b is a reference, not a copy
print a[0, 0, 0]
