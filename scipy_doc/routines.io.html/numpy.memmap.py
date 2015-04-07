import numpy as np

data = np.arange(12, dtype='float32')
data.resize((3, 4))
from tempfile import mkdtemp
import os.path as path

filename = path.join(mkdtemp(), 'newfile.dat')
fp = np.memmap(filename, dtype='float32', mode='w+', shape=(3, 4))
fp
fp[:] = data[:]
fp
fp.filename == path.abspath(filename)
del fp
newfp = np.memmap(filename, dtype='float32', mode='r', shape=(3, 4))
newfp
fpr = np.memmap(filename, dtype='float32', mode='r', shape=(3, 4))
fpr.flags.writeable
fpc = np.memmap(filename, dtype='float32', mode='c', shape=(3, 4))
fpc.flags.writeable
fpc
fpc[0, :] = 0
fpc
fpr
fpo = np.memmap(filename, dtype='float32', mode='r', offset=16)
fpo
