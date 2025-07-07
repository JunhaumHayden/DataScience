"""Modelo SIRV com vacinação constante — usando Runge-Kutta de 4ª ordem."""

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
beta = 0.00033             # Taxa de infecção
gamma = 3. / (15 * 24)     # Taxa de recuperação
nu = 1. / (24 * 50)        # Perda de imunidade (R → S)
p = 0.0001                 # Taxa de vacinação
dt = 0.1                   # Passo de tempo (em horas)
D = 300                    # Duração da simulação (em dias)
N_t = int(D * 24 / dt)     # Total de passos de tempo

print('beta:', beta)

# Tempo e variáveis
t = np.linspace(0, N_t * dt, N_t + 1)
S = np.zeros(N_t + 1)
I = np.zeros(N_t + 1)
R = np.zeros(N_t + 1)
V = np.zeros(N_t + 1)

# Condições iniciais
S[0] = 50
I[0] = 1
R[0] = 0
V[0] = 0

# Equações diferenciais
def dS_dt(S, I, R):
    return -beta * S * I + nu * R - p * S

def dI_dt(S, I):
    return beta * S * I - gamma * I

def dR_dt(I, R):
    return gamma * I - nu * R

def dV_dt(S):
    return p * S

# Método de Runge-Kutta de 4ª ordem
for n in range(N_t):
    S_n, I_n, R_n, V_n = S[n], I[n], R[n], V[n]

    # k1
    k1_S = dt * dS_dt(S_n, I_n, R_n)
    k1_I = dt * dI_dt(S_n, I_n)
    k1_R = dt * dR_dt(I_n, R_n)
    k1_V = dt * dV_dt(S_n)

    # k2
    S_k2 = S_n + 0.5 * k1_S
    I_k2 = I_n + 0.5 * k1_I
    R_k2 = R_n + 0.5 * k1_R
    V_k2 = V_n + 0.5 * k1_V

    k2_S = dt * dS_dt(S_k2, I_k2, R_k2)
    k2_I = dt * dI_dt(S_k2, I_k2)
    k2_R = dt * dR_dt(I_k2, R_k2)
    k2_V = dt * dV_dt(S_k2)

    # k3
    S_k3 = S_n + 0.5 * k2_S
    I_k3 = I_n + 0.5 * k2_I
    R_k3 = R_n + 0.5 * k2_R
    V_k3 = V_n + 0.5 * k2_V

    k3_S = dt * dS_dt(S_k3, I_k3, R_k3)
    k3_I = dt * dI_dt(S_k3, I_k3)
    k3_R = dt * dR_dt(I_k3, R_k3)
    k3_V = dt * dV_dt(S_k3)

    # k4
    S_k4 = S_n + k3_S
    I_k4 = I_n + k3_I
    R_k4 = R_n + k3_R
    V_k4 = V_n + k3_V

    k4_S = dt * dS_dt(S_k4, I_k4, R_k4)
    k4_I = dt * dI_dt(S_k4, I_k4)
    k4_R = dt * dR_dt(I_k4, R_k4)
    k4_V = dt * dV_dt(S_k4)

    # Atualização
    S[n+1] = S_n + (k1_S + 2*k2_S + 2*k3_S + k4_S) / 6
    I[n+1] = I_n + (k1_I + 2*k2_I + 2*k3_I + k4_I) / 6
    R[n+1] = R_n + (k1_R + 2*k2_R + 2*k3_R + k4_R) / 6
    V[n+1] = V_n + (k1_V + 2*k2_V + 2*k3_V + k4_V) / 6

    # Verificação de perda de população (deve ser conservada)
    total_now = V[n+1] + S[n+1] + R[n+1] + I[n+1]
    total_init = V[0] + S[0] + R[0] + I[0]
    loss = int(total_now) - int(total_init)
    if loss > 0:
        print('loss: {:d}'.format(loss))

# Gráfico
fig = plt.figure()
l1, l2, l3, l4 = plt.plot(t, S, t, I, t, R, t, V)
plt.legend((l1, l2, l3, l4), ('S', 'I', 'R', 'V'), loc='upper right')
plt.xlabel('hours')
plt.title('Modelo SIRV com RK4 (vacinação e perda de imunidade)')
plt.grid(True)
plt.savefig('sirv_rk4.pdf')
plt.savefig('sirv_rk4.png')
plt.show()
