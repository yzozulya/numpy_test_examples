import numpy

dst = numpy.array([1, 2])
src = []

numpy.copyto(dst, src, casting='same_kind', where=None)