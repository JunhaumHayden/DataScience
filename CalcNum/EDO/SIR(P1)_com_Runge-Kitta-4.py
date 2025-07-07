import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo
beta = 10. / (40 * 8 * 24)
gamma = 3. / (15 * 24)
dt = 0.1
D = 30  # dias
N_t = int(D * 24 / dt)  # número de passos
t = np.linspace(0, N_t * dt, N_t + 1)

# Inicialização das variáveis
S = np.zeros(N_t + 1)
I = np.zeros(N_t + 1)
R = np.zeros(N_t + 1)

# Condições iniciais
S[0] = 50
I[0] = 1
R[0] = 0

# Funções do sistema SIR
def dS_dt(S, I):
    return -beta * S * I

def dI_dt(S, I):
    return beta * S * I - gamma * I

def dR_dt(I):
    return gamma * I

# Método de Runge-Kutta 4ª ordem
for n in range(N_t):
    S_n, I_n, R_n = S[n], I[n], R[n]

    # k1
    k1_S = dt * dS_dt(S_n, I_n)
    k1_I = dt * dI_dt(S_n, I_n)
    k1_R = dt * dR_dt(I_n)

    # k2
    k2_S = dt * dS_dt(S_n + 0.5 * k1_S, I_n + 0.5 * k1_I)
    k2_I = dt * dI_dt(S_n + 0.5 * k1_S, I_n + 0.5 * k1_I)
    k2_R = dt * dR_dt(I_n + 0.5 * k1_I)

    # k3
    k3_S = dt * dS_dt(S_n + 0.5 * k2_S, I_n + 0.5 * k2_I)
    k3_I = dt * dI_dt(S_n + 0.5 * k2_S, I_n + 0.5 * k2_I)
    k3_R = dt * dR_dt(I_n + 0.5 * k2_I)

    # k4
    k4_S = dt * dS_dt(S_n + k3_S, I_n + k3_I)
    k4_I = dt * dI_dt(S_n + k3_S, I_n + k3_I)
    k4_R = dt * dR_dt(I_n + k3_I)

    # Atualização
    S[n+1] = S_n + (k1_S + 2*k2_S + 2*k3_S + k4_S) / 6
    I[n+1] = I_n + (k1_I + 2*k2_I + 2*k3_I + k4_I) / 6
    R[n+1] = R_n + (k1_R + 2*k2_R + 2*k3_R + k4_R) / 6

# Gráfico
fig = plt.figure()
l1, l2, l3 = plt.plot(t, S, t, I, t, R)
plt.legend((l1, l2, l3), ('S', 'I', 'R'), loc='center right')
plt.xlabel('hours')
plt.title('SIR com Runge-Kutta de 4ª ordem')
plt.grid(True)
plt.savefig('sir_rk4.pdf')
plt.savefig('sir_rk4.png')
plt.show()
