import numpy as np

a = np.ma.MaskedArray()
fid = open('')
a.tofile(fid, sep='', format='%s')