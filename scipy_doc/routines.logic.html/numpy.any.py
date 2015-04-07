import numpy as np

np.any([[True, False], [True, True]])
np.any([[True, False], [False, False]], axis=0)
np.any([-1, 0, 5])
np.any(np.nan)
o = np.array([False])
z = np.any([-1, 4, 5], out=o)
z, o
# Check now that z is a reference to o
z is o
id(z), id(o)  # identity of z and o
