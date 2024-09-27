import numpy as np
import matplotlib.pyplot as plt


def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    return x, y

Vreg, Vo3 = procesarPuntos('resources/RtaLinea3.txt')

Vreg, Vo5 = procesarPuntos('resources/RtaLinea5.txt')


fig1 = plt.figure()
plt.grid(True)

plt.xlabel('Tensión de entrada [V]')
plt.ylabel('Tensión de salida[V]')
plt.title('Rectas de Linea')
plt.plot(Vreg, Vo3,color='darkorchid',label = 'Vo = 3.3V',linewidth=3)
plt.plot(Vreg, Vo5, color='#e377c2', label = 'Vo = 5V',linewidth=3)

plt.legend()
plt.savefig('graficos/rectasDeLinea.png')

plt.show()