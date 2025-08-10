import numpy as np

#SOR para um exemplo de sistema tridiagonal
w = 1.26
n = 4

x0 = np.zeros(n)
x = np.zeros(n)

it = 1
itmax = 1000
tol = 1.0e-6
dmax = 1

while(dmax > tol and it < itmax):
  x[0] = (1 - w)*x0[0] + w*(1 + x0[1])/2
  for i in range(1,n-1):
    x[i] = (1 - w)*x0[i] + w*(x[i-1] + x0[i+1])/2
  
  x[n-1] = (1 - w)*x0[n-1] + w*(1 + x[n-2])/2
  dmax = max(abs(x - x0))
  x0 = np.copy(x)
  
  it = it + 1

print(it, dmax, x)
