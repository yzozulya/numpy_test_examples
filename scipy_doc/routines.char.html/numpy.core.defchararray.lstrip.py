import numpy as np

c = np.array(['aAaAaA', '  aA  ', 'abBABba'])
c
np.char.lstrip(c, 'a')
np.char.lstrip(c, 'A')  # leaves c unchanged
(np.char.lstrip(c, ' ') == np.char.lstrip(c, '')).all()
# XXX: is this a regression? this line now returns False
# np.char.lstrip(c,'') does not modify c at all.
(np.char.lstrip(c, ' ') == np.char.lstrip(c, None)).all()
