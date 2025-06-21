#Interpolação linear por partes
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def f(x):
  y = 1/(1 + x**2)
  return y

n = 16
x = np.zeros(n+1)
a = -4
b = 4
h = (b - a)/n
x[0] = a
for i in range(1,n+1):
  x[i] = x[i-1] + h
#print(x)
y = f(x)

p = sp.interpolate.interp1d(x,y)
xx = np.linspace(x[0],x[n],51)
yy = p(xx)

plt.figure(1)
plt.plot(x, y, 'bo', xx, yy)
plt.show()

