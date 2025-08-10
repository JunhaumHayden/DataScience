import numpy as np

def f(x):
    return 1/x

a = 1
b = 2

N = 4 # quantidade de subintervalos
h = (b-a)/N
x = np.linspace(a,b,N+1)

#Retangulo : altura f(a)
soma = 0
for i in range(N):
    soma += f(x[i])
IR = h*soma

print("Erro = ", abs(np.log(2) - IR))
print("IR = ", IR)

#Retangulo : altura f(b)
soma = 0
for i in range(N):
    soma += f(x[i+1])
IR = h*soma

print("Erro = ", abs(np.log(2) - IR))
print("IR = ", IR)

#Retangulo : altura f(x_m)
soma = 0
for i in range(N):
    xm = (x[i] + x[i+1])/2
    soma += f(xm)
IR = h*soma

print("Erro = ", abs(np.log(2) - IR))
print("IR = ", IR)
