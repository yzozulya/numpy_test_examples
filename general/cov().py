from numpy import *

x = array([1., 3., 8., 9.])
variance = cov(x)  # normalized by N-1
variance = cov(x, bias=1)  # normalized by N
T = array([1.3, 4.5, 2.8, 3.9])  # temperature measurements
P = array([2.7, 8.7, 4.7, 8.2])  # corresponding pressure measurements
cov(T, P)  # covariance between temperature and pressure
rho = array([8.5, 5.2, 6.9, 6.5])  # corresponding density measurements
data = column_stack([T, P, rho])
print cov(data)  # covariance matrix of T,P and rho
