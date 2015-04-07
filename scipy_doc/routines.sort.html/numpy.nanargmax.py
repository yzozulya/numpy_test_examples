import numpy as np

a = np.array([[np.nan, 4], [2, 3]])
np.argmax(a)
np.nanargmax(a)
np.nanargmax(a, axis=0)
np.nanargmax(a, axis=1)
