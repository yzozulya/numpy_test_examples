import numpy as np

np.sinh(0)
np.sinh(np.pi * 1j / 2)
np.sinh(np.pi * 1j)  # (exact value is 0)
# Discrepancy due to vagaries of floating point arithmetic.
# Example of providing the optional output parameter
out1 = np.array([0.1])
out2 = np.sinh([0.1], out1)
out2 is out1
# Example of ValueError due to provision of shape mis-matched `out`
np.sinh(np.zeros((3, 3)), np.zeros((2, 2)))
