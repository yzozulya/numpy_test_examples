import numpy as np

np.dtype(np.int16)
np.dtype([('f1', np.int16)])
np.dtype([('f1', [('f1', np.int16)])])
np.dtype([('f1', np.uint), ('f2', np.int32)])
np.dtype([('a', 'f8'), ('b', 'S10')])
np.dtype("i4, (2,3)f8")
np.dtype([('hello', (np.int, 3)), ('world', np.void, 10)])
np.dtype((np.int16, {'x': (np.int8, 0), 'y': (np.int8, 1)}))
np.dtype({'names': ['gender', 'age'], 'formats': ['S1', np.uint8]})
np.dtype({'surname': ('S25', 0), 'age': (np.uint8, 25)})
