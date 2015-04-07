import numpy as np

np.cos(np.array([0, np.pi / 2, np.pi]))
# Example of providing the optional output parameter
out2 = np.cos([0.1], out1)
out2 is out1
# Example of ValueError due to provision of shape mis-matched `out`
np.cos(np.zeros((3, 3)), np.zeros((2, 2)))
