import numpy as np

def f(x):
    return 1/x

a = 1
b = 2

N = 32 # quantidade de subintervalos
h = (b-a)/N
x = np.linspace(a,b,N+1)

#Simpson
soma = 0
for i in range(1,N,2):
    soma += 2*f(x[i]) + f(x[i+1])
IS = (h/3)*(2*soma + f(x[0]) - f(x[N]))

print("Erro = ", abs(np.log(2) - IS))
print("IS = ", IS)
