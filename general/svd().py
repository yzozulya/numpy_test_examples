from numpy import *
from numpy.linalg import svd

A = array([[1., 3., 5.], [2., 4., 6.]])  # A is a (2x3) matrix
U, sigma, V = svd(A)
print U  # U is a (2x2) unitary matrix
print sigma  # non-zero diagonal elements of Sigma
print V  # V is a (3x3) unitary matrix
Sigma = zeros_like(A)  # constructing Sigma from sigma
n = min(A.shape)
Sigma[:n, :n] = diag(sigma)
print dot(U, dot(Sigma, V))  # A = U * Sigma * V
