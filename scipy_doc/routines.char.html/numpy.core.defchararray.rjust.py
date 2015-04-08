import numpy

a = numpy.array(['1', '2'])
width = 1

numpy.core.defchararray.rjust(a, width, fillchar=' ')
