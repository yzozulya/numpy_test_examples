import numpy as np

c = np.array(['aAaAaA', '  aA  ', 'abBABba'])
c
np.char.strip(c)
np.char.strip(c, 'a')  # 'a' unstripped from c[1] because whitespace leads
np.char.strip(c, 'A')  # 'A' unstripped from c[1] because (unprinted) ws trails
