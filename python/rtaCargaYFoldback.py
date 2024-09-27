import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

#color='#5ce9ff'

def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    z = datos_simul[:, 2]
    return x, y,z

RL,Vo3,Io3=procesarPuntos('resources/stepRL3V.txt')
RL,Vo5,Io5=procesarPuntos('resources/stepRL5V.txt')

fig1 = plt.figure()
plt.grid(True)

plt.xlabel('RL [$\Omega$]')
plt.ylabel('Tensión de salida[V]')
plt.title('Rectas de carga')
plt.plot(RL, Vo3,color='darkorchid',label = 'Vo = 3.3V',linewidth=3)
plt.plot(RL, Vo5, color='#e377c2', label = 'Vo = 5V',linewidth=3)

plt.legend()
plt.savefig('graficos/rectasDeCarga.png')


fig2 = plt.figure()
plt.grid(True)

plt.xlabel('$I_{RL}$ [mA]')
plt.ylabel('Tensión de salida [V]')
plt.title('Foldback')
plt.plot(Io3*10**3,Vo3,color='darkorchid',label = 'Vo = 3.3V',linewidth=3)
plt.plot(Io5*10**3, Vo5, color='#e377c2', label = 'Vo = 5V',linewidth=3)

plt.legend()
plt.savefig('graficos/Foldbacks.png')





plt.show()