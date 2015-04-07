import numpy as np

deg = np.arange(12.) * 30.
np.radians(deg)
out = np.zeros(deg.shape)
ret = np.radians(deg, out)
ret is out
