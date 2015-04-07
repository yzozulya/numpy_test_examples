import numpy as np

x = np.arange(9)
y1, y2 = np.frexp(x)
y1
y2
y1 * 2 ** y2
