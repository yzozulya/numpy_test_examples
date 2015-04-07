from numpy import *

x = array([pi, 1.e-200])
x
set_printoptions(precision=3, suppress=True)  # 3 digits behind decimal point + suppress small values
x
help(set_printoptions)  # see help() for keywords 'threshold','edgeitems' and 'linewidth'
