import numpy as np

dt = np.dtype(int)
dt = dt.newbyteorder('>')
buf = '1'
np.frombuffer(buf, dtype=dt)
s = 'hello world'
np.frombuffer(s, dtype='S1', count=5, offset=6)
