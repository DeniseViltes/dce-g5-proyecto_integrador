import numpy as np
import matplotlib.pyplot as plt

def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    return x, y


tiempo, vo3_r1 = procesarPuntos('resources/transitorio-foldback3-Rl1.txt')
tiempo3, vo3_r4_3 = procesarPuntos('resources/transitorio-foldback3-Rl4-3.txt')

tiempo4, vo5_r1 = procesarPuntos('resources/transitorio-foldback5-Rl1.txt')
tiempo6, vo5_r6_6 = procesarPuntos('resources/transitorio-foldback5-Rl5.txt')


fig1 = plt.figure()
plt.grid(True)

plt.xlabel('Tiempo [ms]')
plt.ylabel('Tensión de salida [V]')
plt.title('Respuesta al escalón con Foldback activado para $V_o= 3 V$')
plt.plot(tiempo*10**3, vo3_r1,color='darkorchid',linewidth=3)

plt.savefig('graficos/TransitorioFoldaback3.png')


fig2 = plt.figure()
plt.grid(True)

plt.xlabel('Tiempo [ms]')
plt.ylabel('Tensión de salida [V]')
plt.title('Respuesta al escalón con Foldback activado para $V_o= 5 V$')
plt.plot(tiempo4*10**3, vo5_r1,color='#e377c2',linewidth=3)

plt.savefig('graficos/TransitorioFoldaback5.png')
plt.show()

