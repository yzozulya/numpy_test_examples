import numpy as np

A = np.mat('1 1; 1 1')
B = np.mat('2 2; 2 2')
C = np.mat('3 4; 5 6')
D = np.mat('7 8; 9 0')
np.bmat([[A, B], [C, D]])
np.bmat(np.r_[np.c_[A, B], np.c_[C, D]])
np.bmat('A,B; C,D')
