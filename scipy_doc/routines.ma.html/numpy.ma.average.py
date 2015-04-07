import numpy as np

a = np.ma.array([1., 2., 3., 4.], mask=[False, False, True, True])
np.ma.average(a, weights=[3, 1, 0, 0])
x = np.ma.arange(6.).reshape(3, 2)
print
x
avg, sumweights = np.ma.average(x, axis=0, weights=[1, 2, 3],
                                returned=True)
print
avg
