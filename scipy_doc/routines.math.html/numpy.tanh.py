import numpy as np

np.tanh((0, np.pi * 1j, np.pi * 1j / 2))
# Example of providing the optional output parameter illustrating
# that what is returned is a reference to said parameter
out1 = np.array([0.1])
out2 = np.tanh([0.1], out1)
out2 is out1
# Example of ValueError due to provision of shape mis-matched `out`
np.tanh(np.zeros((3, 3)), np.zeros((2, 2)))
