# Método de Newton e suas modificações
import numpy as np

# Teste 1: f(x) = x**2 - 2
# Teste 2: f(x) = e^x - x - 1. Exemplo que o método perde a convergencia quadrática

def f(x):
    #return x**2 - 2
    return np.exp(x) - x - 1

# Teste 1: f'(x)=2x
# Teste 2: f'(x) = e^x - 1 
def df(x):
    #return 2*x
    return np.exp(x) - 1

#Teste 2: f''(x) = e^x , pois usamos a regra de L'hopital
def ddf(x):
    return np.exp(x)
    

def newton(x0):
    tol = 1.0e-8
    it = 1
    itmax = 100

    while(abs(f(x0)) > tol and it < itmax):
        x = x0 - f(x0)/df(x0)
        #print(it, x, abs(f(x)))
        x0 = x
        it += 1
    return it-1,x

def newton_modificado(x0):
    tol = 1.0e-8
    it = 1
    itmax = 100
    df0 = df(x0)
    while(abs(f(x0)) > tol and it < itmax):
        x = x0 - f(x0)/df0
        #print(it, x, abs(f(x)))
        x0 = x
        it += 1
    return it-1, x

def secante(x0, x1):
    tol = 1.0e-8
    it = 1
    itmax = 100
    while(abs(f(x1)) > tol and it < itmax):
        x = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
        #print(it, x, abs(f(x)))
        x0 = x1
        x1 = x
        it += 1
    return it-1, x

def newton_lhopital(x0):
    tol = 1.0e-8
    it = 1
    itmax = 100
    while(abs(f(x0)) > tol and it < itmax):
        x = x0 - df(x0)/ddf(x0)
        #print(it, x, abs(f(x)))
        x0 = x
        it += 1
    return it-1, x

def teste1():
    #Teste 1: f(x)=x^2-2
    x0 = 1.3
    k, x = newton(x0)
    print("Raiz aproximada Newton: ", x, " com ", k, " iterações")
    x0 = 1.3
    k, x = newton_modificado(x0)
    print("Raiz aproximada Newton Modificado: ", x, " com ", k, " iterações")
    x0 = 1.3
    x1 = 1.7
    k, x = newton_modificado(x0)
    print("Raiz aproximada Secante: ", x, " com ", k, " iterações")

def teste2():
    #Teste 2
    x0 = 1
    k, x = newton(x0)
    print("Raiz aproximada newton: ", x, " com ", k, " iterações")
    x0 = 1
    k, x = newton_lhopital(x0)
    print("Raiz aproximada newton: ", x, " com ", k, " iterações")
    

#teste1()

teste2()


      
