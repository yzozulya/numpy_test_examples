import numpy as np
from tempfile import TemporaryFile

a = np.empty(10, dtype='f8,i4,a5')
a[5] = (0.5, 10, 'abcde')
fd = TemporaryFile()
a = a.newbyteorder('<')
a.tofile(fd)
fd.seek(0)
r = np.core.records.fromfile(fd, formats='f8,i4,a5', shape=10,
                             byteorder='<')
print
r[5]
r.shape
