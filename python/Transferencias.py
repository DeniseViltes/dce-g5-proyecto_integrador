import numpy as np
import matplotlib.pyplot as plt


def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    z = datos_simul[:, 2]
    return x, y,z



freq,mag,fase = procesarPuntos('resources/Sin-compensar/Vf5-Rl10.txt')

fig1, ax1 = plt.subplots()
plt.grid(True)

ax1.set_xlabel('Frequencia [Hz]')
ax1.set_xscale('log')

# acomodar los ejes


ax1.set_ylabel('Ganancia [dB]',color = 'darkorchid')
# plt.title('Etapa amplificadora con un transistor')

plot_1 = ax1.plot(freq, mag,color='darkorchid',linewidth=3)

ax2 = ax1.twinx()
ax2.set_ylabel('Fase [°]',color = '#e377c2')
plot_2 = ax2.plot(freq, fase,color='#e377c2' ,linewidth=1,linestyle='dashed')

lns = plot_1 + plot_2
labels = [l.get_label() for l in lns]
# plt.legend(lns, labels, loc=0)

plt.savefig('graficos/TransferenciaLazoTensionSinCompensar.png')

plt.show()