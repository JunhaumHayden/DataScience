import matplotlib.pyplot as plt
import numpy as np

def f(x):
  y = 1/(1 + x**2)
  return y
# coeficientes do polinomio via tabela de Diferenças Divididas
def dif_div(x, y):
  n = len(x)
  D = np.zeros((n,n))
  c = np.zeros(n)
  for i in range(n):
    D[i][0] = y[i]
  for j in range(1,n):
    for i in range(n-j):
      D[i][j] = (D[i+1][j-1] - D[i][j-1])/(x[i+j] - x[i])
  #print(D)
  for i in range(n):
    c[i] = D[0][i] 

  return c

# Avaliação do polinomio na forma de Newton
def p(x, xt, c):
  n = len(c)
  vp = np.zeros(n)
  vp[0] = c[0]
  px = 0
  ss = 1
  for i in range(1,n):
    ss = ss*(x - xt[i-1])
    vp[i] = c[i]*ss
  for i in range(n):
    px = px + vp[i]
  return px

# Fenêomeno de Runge
n = 4
x = np.zeros(n+1)
a = -4
b = 4
h = (b - a)/n
x[0] = a
for i in range(1,n+1):
  x[i] = x[i-1] + h
#print(x)
y = f(x)
c = dif_div(x, y)

xx = np.linspace(x[0],x[n],100)
m = len(xx)
yy = np.zeros(m)
for i in range(m):
  yy[i] = p(xx[i], x, c)


plt.figure(1)
plt.plot(x,f(x),'bo')
plt.plot(xx, yy)
plt.plot(xx,f(xx),'r-.')
plt.show()
