import numpy as np

c = np.array(['aAaAaA', '  aA  ', 'abBABba'])
c
np.char.count(c, 'A')
np.char.count(c, 'aA')
np.char.count(c, 'A', start=1, end=4)
np.char.count(c, 'A', start=1, end=3)
