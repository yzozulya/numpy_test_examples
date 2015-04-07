import numpy as np
from numpy import degrees

rad = np.arange(12.) * np.pi / 6
np.degrees(rad)
out = np.zeros(rad.shape)
r = degrees(rad, out)
np.all(r == out)
