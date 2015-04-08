import numpy as np

a = np.ma.MaskedArray()
a.resize((1, 2, 3), refcheck=True, order=False)