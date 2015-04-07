import numpy as np

c = np.array(['aAaAaA', '  aA  ', 'abBABba'])
c
np.char.encode(c, encoding='cp037')
