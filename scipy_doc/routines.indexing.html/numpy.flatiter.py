import numpy as np

x = np.arange(6).reshape(2, 3)
fl = x.flat
type(fl)
for item in fl:
    print
    item
fl[2:4]
