import numpy

rate = [1, 2, 3]
per = 1
nper = [1, 2, 2]
pv = [1, 2, 4]
numpy.ppmt(rate, per, nper, pv, fv=0.0, when='end')