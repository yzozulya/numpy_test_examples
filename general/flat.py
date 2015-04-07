from numpy import *

a = array([[10, 30], [40, 60]])
iter = a.flat  # .flat returns an iterator
iter.next()  # cycle through array with .next()
iter.next()
iter.next()
