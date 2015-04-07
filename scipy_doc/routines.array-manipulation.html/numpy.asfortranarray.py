import numpy as np

x = np.arange(6).reshape(2, 3)
y = np.asfortranarray(x)
x.flags['F_CONTIGUOUS']
y.flags['F_CONTIGUOUS']
