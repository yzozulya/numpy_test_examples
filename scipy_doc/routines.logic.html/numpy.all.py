import numpy as np

np.all([[True, False], [True, True]])
np.all([[True, False], [True, True]], axis=0)
np.all([-1, 4, 5])
np.all([1.0, np.nan])
o = np.array([False])
z = np.all([-1, 4, 5], out=o)
id(z), id(o), z                             
