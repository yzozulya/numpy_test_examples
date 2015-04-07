import numpy as np

typechars = ['S1', '?', 'B', 'D', 'G', 'F', 'I', 'H', 'L', 'O', 'Q',
             'S', 'U', 'V', 'b', 'd', 'g', 'f', 'i', 'h', 'l', 'q']
for typechar in typechars:
    print
    typechar, ' : ', np.typename(typechar)
