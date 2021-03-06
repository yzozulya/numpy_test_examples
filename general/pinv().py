from numpy import *
from numpy.linalg import pinv, svd, lstsq

A = array([[1., 3., 5.], [2., 4., 6.]])
b = array([1., 3.])
# Question: find x such that ||A*x-b|| is minimal
# Answer: x = pinvA * b, with pinvA the pseudo-inverse of A
pinvA = pinv(A)
print pinvA
x = dot(pinvA, b)
print x
# Relation with least-squares minimisation lstsq()
x, resids, rank, s = lstsq(A, b)
print x  # the same solution for x as above
# Relation with singular-value decomposition svd()
U, sigma, V = svd(A)
S = zeros_like(A.transpose())
for n in range(len(sigma)):
    S[n, n] = 1. / sigma[n]
dot(V.transpose(), dot(S, U.transpose()))  # = pinv(A)
