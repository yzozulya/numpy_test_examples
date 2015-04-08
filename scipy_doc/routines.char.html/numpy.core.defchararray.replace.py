import numpy

a = numpy.array(['1', '2'])
old = '1'
new = '2'

numpy.core.defchararray.replace(a, old, new, count=None)