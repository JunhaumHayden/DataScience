"""Modelo SIRS com perda de imunidade — usando Runge-Kutta de 4ª ordem."""

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
beta = 0.00043              # Taxa de infecção
gamma = 3. / (15 * 24)      # Taxa de recuperação
nu = 1. / (24 * 90)         # Perda de imunidade (R → S)
dt = 0.1                    # Passo (em horas)
D = 300                     # Duração da simulação (em dias)
N_t = int(D * 24 / dt)      # Total de passos

# Vetor de tempo e variáveis
t = np.linspace(0, N_t * dt, N_t + 1)
S = np.zeros(N_t + 1)
I = np.zeros(N_t + 1)
R = np.zeros(N_t + 1)

# Condições iniciais
S[0] = 50
I[0] = 1
R[0] = 0

# Equações diferenciais do modelo SIRS
def dS_dt(S, I, R):
    return -beta * S * I + nu * R

def dI_dt(S, I):
    return beta * S * I - gamma * I

def dR_dt(I, R):
    return gamma * I - nu * R

# Método de Runge-Kutta 4ª ordem
for n in range(N_t):
    S_n, I_n, R_n = S[n], I[n], R[n]

    # k1
    k1_S = dt * dS_dt(S_n, I_n, R_n)
    k1_I = dt * dI_dt(S_n, I_n)
    k1_R = dt * dR_dt(I_n, R_n)

    # k2
    S_k2 = S_n + 0.5 * k1_S
    I_k2 = I_n + 0.5 * k1_I
    R_k2 = R_n + 0.5 * k1_R

    k2_S = dt * dS_dt(S_k2, I_k2, R_k2)
    k2_I = dt * dI_dt(S_k2, I_k2)
    k2_R = dt * dR_dt(I_k2, R_k2)

    # k3
    S_k3 = S_n + 0.5 * k2_S
    I_k3 = I_n + 0.5 * k2_I
    R_k3 = R_n + 0.5 * k2_R

    k3_S = dt * dS_dt(S_k3, I_k3, R_k3)
    k3_I = dt * dI_dt(S_k3, I_k3)
    k3_R = dt * dR_dt(I_k3, R_k3)

    # k4
    S_k4 = S_n + k3_S
    I_k4 = I_n + k3_I
    R_k4 = R_n + k3_R

    k4_S = dt * dS_dt(S_k4, I_k4, R_k4)
    k4_I = dt * dI_dt(S_k4, I_k4)
    k4_R = dt * dR_dt(I_k4, R_k4)

    # Atualização
    S[n+1] = S_n + (k1_S + 2*k2_S + 2*k3_S + k4_S) / 6
    I[n+1] = I_n + (k1_I + 2*k2_I + 2*k3_I + k4_I) / 6
    R[n+1] = R_n + (k1_R + 2*k2_R + 2*k3_R + k4_R) / 6

# Gráfico
fig = plt.figure()
l1, l2, l3 = plt.plot(t, S, t, I, t, R)
plt.legend((l1, l2, l3), ('S', 'I', 'R'), loc='upper right')
plt.xlabel('hours')
plt.title('Modelo SIRS com RK4')
plt.grid(True)
plt.savefig('sirs_rk4.pdf')
plt.savefig('sirs_rk4.png')
plt.show()
