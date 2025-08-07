#Exemplo Spline Cúbico
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def f(x):
    return 1/(1+x**2)

n = 8
x = np.zeros(n+1)
a = -4
b = 4
h = (b - a)/n
x[0] = a
for i in range(1,n+1):
  x[i] = x[i-1] + h
#print(x)
y = f(x)

sc = sp.interpolate.CubicSpline(x,y)

xx = np.linspace(a,b,100)
yy = sc(xx)

plt.figure(1)
plt.plot(x, y, 'bo', xx, yy,'b--', xx, f(xx),'r-.')
plt.show()

