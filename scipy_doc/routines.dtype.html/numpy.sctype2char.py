import numpy as np

for sctype in [np.int32, np.float, np.complex, np.string_, np.ndarray]:
    print
    np.sctype2char(sctype)
x = np.array([1., 2 - 1.j])
np.sctype2char(x)
np.sctype2char(list)
