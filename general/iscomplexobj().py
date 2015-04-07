import numpy as np

a = np.array([1, 2, 3.j])
np.iscomplexobj(a)
a = np.array([1, 2, 3])
np.iscomplexobj(a)
a = np.array([1, 2, 3], dtype=np.complex)
np.iscomplexobj(a)
