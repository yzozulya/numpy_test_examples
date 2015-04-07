from numpy import *

serialnr = array([1023, 5202, 6230, 1671, 1682, 5241])
height = array([40., 42., 60., 60., 98., 40.])
width = array([50., 20., 70., 60., 15., 30.])
# We want to sort the serial numbers with increasing height, _AND_
# serial numbers with equal heights should be sorted with increasing width.
indices = lexsort(keys=(width, height))  # mind the order!
indices
for n in indices:
    print serialnr[n], height[n], width[n]
a = vstack([serialnr, width, height])  # Alternatively: all data in one big matrix
print a  # Mind the order of the rows!
indices = lexsort(a)  # Sort on last row, then on 2nd last row, etc.
a.take(indices, axis=-1)
