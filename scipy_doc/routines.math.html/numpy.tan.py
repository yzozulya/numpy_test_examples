import numpy as np
from math import pi

np.tan(np.array([-pi, pi / 2, pi]))
# Example of providing the optional output parameter illustrating
# that what is returned is a reference to said parameter
out2 = np.cos([0.1], out1)
out2 is out1
# Example of ValueError due to provision of shape mis-matched `out`
np.cos(np.zeros((3, 3)), np.zeros((2, 2)))
