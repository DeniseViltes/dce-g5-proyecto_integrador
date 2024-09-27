import numpy as np
import matplotlib.pyplot as plt

def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    return x, y



tiempo, vf3_R10 = procesarPuntos('resources/transitorio-Vf3-R10.txt')

tiempo2, vf5_R10 = procesarPuntos('resources/transitorio-Vf5-R10.txt')



fig1, ax1 = plt.subplots()
plt.grid(True)

ax1.set_xlabel('Tiempo [m s]')
ax1.set_ylabel('Tensión [V]',color = 'darkorchid')
plt.title('Respuesta temporal del lazo de tension')

plot_1 = ax1.plot(tiempo*10**3, vf3_R10,color='darkorchid',label = '$V_o = 3V$' ,linewidth=3,linestyle='dashed')

ax2 = ax1.twinx()
ax2.set_ylabel('Tensión [mV]',color = '#e377c2')
plot_2 = ax2.plot(tiempo2*10**3, vf5_R10,color='#e377c2',label = '$V_o = 5V$',linewidth=1)

lns = plot_1 + plot_2
labels = [l.get_label() for l in lns]
plt.legend(lns, labels, loc=0)

plt.savefig('graficos/TransitoriosGananciaTension.png')


tiempo, Vlc_R6_8 = procesarPuntos('resources/transitorio-Vlc-R6.8.txt')
tiempo2, Vlc_R4_4 = procesarPuntos('resources/transitorio-Vlc-R44.txt')



fig2, ax1 = plt.subplots()
plt.grid(True)

ax1.set_xlabel('Tiempo [m s]')
ax1.set_ylabel('Tensión [V]',color = 'darkorchid')
plt.title('Respuesta temporal del lazo de corriente')

plot_1 = ax1.plot(tiempo2*10**3, Vlc_R4_4,color='darkorchid',label = '$V_o = 3V$',linewidth=3,linestyle='dashed')

ax2 = ax1.twinx()
ax2.set_ylabel('Tensión [V]',color = '#e377c2')
plot_2 = ax2.plot(tiempo*10**3, Vlc_R6_8,color='#e377c2',label = '$V_o = 5V$' ,linewidth=1)

lns = plot_1 + plot_2
labels = [l.get_label() for l in lns]
plt.legend(lns, labels, loc=0)

plt.savefig('graficos/TransitoriosGananciaCorriente.png')




plt.show()

