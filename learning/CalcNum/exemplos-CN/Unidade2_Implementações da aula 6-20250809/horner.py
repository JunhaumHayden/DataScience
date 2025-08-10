#Método de Horner para avaliar polinomio + método de Newton

def horner(x0, a):
    n = len(a)
    # y representa p(x0)
    # z representa p'(x0)
    y = a[n-1]
    z = a[n-1]
    for j in range(n-2,0,-1):
        y = x0*y + a[j]
        z = x0*z + y
    y = x0*y + a[0]
    return y, z

def newton_horner(x0, a):
    tol = 1.0e-8
    it = 1
    itmax = 100
    y = 1 # y = p(x0)
    while(abs(y) > tol and it < itmax):
        y, z = horner(x0, a)
        x = x0 - y/z
        x0 = x
        print(it, x, y, z)
        it += 1

# Teste: p(x) = 2x^4-3x^2+3x-4

#O vetor a armazena os coeficientes do polinômio

a = [-4, 3, -3, 2]
x0 = 2
newton_horner(x0, a)
        
