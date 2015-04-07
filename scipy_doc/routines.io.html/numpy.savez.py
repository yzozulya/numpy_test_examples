import numpy as np
from tempfile import TemporaryFile

outfile = TemporaryFile()
x = np.arange(10)
y = np.sin(x)
np.savez(outfile, x, y)
outfile.seek(0)  # Only needed here to simulate closing & reopening file
npzfile = np.load(outfile)
npzfile.files
npzfile['arr_0']
outfile = TemporaryFile()
np.savez(outfile, x=x, y=y)
outfile.seek(0)
npzfile = np.load(outfile)
npzfile.files
npzfile['x']
