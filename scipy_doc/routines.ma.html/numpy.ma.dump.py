import numpy
from numpy.ma import MaskedArray

a = MaskedArray()
F = ''
numpy.ma.dump(a, F)