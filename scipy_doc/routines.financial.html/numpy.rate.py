import numpy

rate = [1, 2, 3]
per = 1
pmt = [1, 2]
nper = [1, 2, 2]
pv = [1, 2, 4]
fv = [1, 2, 4]

numpy.rate(nper, pmt, pv, fv, when='end', guess=0.1, tol=1e-06, maxiter=100)