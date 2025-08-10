import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(s, ".")
ax.set(xlabel='i', ylabel='s',
       title='Exemplo 1')


fig.savefig("test.png")
plt.show()

fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='t', ylabel='s=f(t)',
       title='Exemplo 2')
ax.grid()
plt.show()

#Para mais exemplos de gráficos veja:
#https://matplotlib.org/stable/gallery/index.html
