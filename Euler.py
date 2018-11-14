import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *

a, b = symbols("x y")
f = lambda t: 2*t
y = np.zeros(11)
n, h = 10, 1.0
ite = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Euler
i=0
hi=0
for j in range(10):
    y[i + 1] = y[i] + h * f(hi)
    print('y[%d]=%f' % (i+1, y[i+1]))
    i += 1
    hi += h
print(y)

a = np.arange(0,10,0.01)
b = a ** 2
plt.plot(a, b)
for j in range(10):
    plt.plot(j + 1, y[j + 1], ".r")
plt.show()

h = 0.1
y = np.zeros(11)
f = lambda u,v : v+-12*u+3
y[0]=1.0
#Euler
i, hi = 0, 0.0
for j in range(10):
    y[i+1] = y[i] + h * f(hi,y[i])
    print('y[%d]=%f' % (i+1, y[i+1]))
    i += 1
    hi += h
print(y)

a = np.arange(0,1,0.01)
plt.plot(a,-8*np.exp(a)+12*a+9)
hi=0.1
for j in range(10):
    plt.plot(hi,y[j+1],".r")
    hi=hi+h
plt.show()
