import numpy as np

dt = np.dtype([('time', [('min', int), ('sec', int)]),
               ('temp', float)])
x = np.zeros((1,), dtype=dt)
x['time']['min'] = 10
x['temp'] = 98.25
x
import os

fname = os.tmpnam()
x.tofile(fname)
np.fromfile(fname, dtype=dt)
np.save(fname, x)
np.load(fname + '.npy')
