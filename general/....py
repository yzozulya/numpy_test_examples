from numpy import *

a = arange(12)
a = a.reshape(3, 2, 2)
print a
a[..., 0]  # same as a[:,:,0]
a[1:, ...]  # same as a[1:,:,:] or just a[1:]
