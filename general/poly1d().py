from numpy import *

p1 = poly1d([2, 3], r=1)  # specify polynomial by its roots
print p1
p2 = poly1d([2, 3], r=0)  # specify polynomial by its coefficients
print p2
print p1 + p2  # +,-,*,/ and even ** are supported
quotient, remainder = p1 / p2  # division gives a tupple with the quotient and remainder
print quotient, remainder
p3 = p1 * p2
print p3
p3([1, 2, 3, 4])  # evaluate the polynomial in the values [1,2,3,4]
p3[2]  # the coefficient of x**2
p3.r  # the roots of the polynomial
p3.c  # the coefficients of the polynomial
p3.o  # the order of the polynomial
print p3.deriv(m=2)  # the 2nd derivative of the polynomial
print p3.integ(m=2, k=[1, 2])  # integrate polynomial twice and use [1,2] as integration constants
