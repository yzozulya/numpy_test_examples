import numpy as np

a = np.random.randn(9, 6)
q, r = np.linalg.qr(a)
np.allclose(a, np.dot(q, r))  # a does equal qr
r2 = np.linalg.qr(a, mode='r')
r3 = np.linalg.qr(a, mode='economic')
np.allclose(r, r2)  # mode='r' returns the same r as mode='full'
# But only triu parts are guaranteed equal when mode='economic'
np.allclose(r, np.triu(r3[:6, :6], k=0))
A = np.array([[0, 1], [1, 1], [1, 1], [2, 1]])
A
b = np.array([1, 0, 2, 1])
q, r = LA.qr(A)
p = np.dot(q.T, b)
np.dot(LA.inv(r), p)
