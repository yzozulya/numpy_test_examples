import numpy as np

marr = np.ma.array(np.arange(10), mask=[0, 0, 0, 1, 1, 1, 0, 0, 0, 0])
print
marr.cumsum()
