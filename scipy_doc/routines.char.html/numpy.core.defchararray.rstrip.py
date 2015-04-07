import numpy as np

c = np.array(['aAaAaA', 'abBABba'], dtype='S7')
c
np.char.rstrip(c, 'a')
np.char.rstrip(c, 'A')
