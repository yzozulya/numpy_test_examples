from numpy import *

a = array([[1, 2], [3, 4]])
b = array([5, 6])
c = broadcast(a, b)
c.nd  # the number of dimensions in the broadcasted result
c.shape  # the shape of the broadcasted result
c.size  # total size of the broadcasted result
for value in c:
    print value
c.reset()  # reset the iterator to the beginning
c.next()  # next element
