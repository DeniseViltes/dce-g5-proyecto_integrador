import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True


def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    return x, y


RL,p3 = procesarPuntos('resources/potencia-vo3.txt')
RL,p5 = procesarPuntos('resources/potencia-vo5.txt')

fig1 = plt.figure()
plt.grid(True)

plt.xlabel('Rl [$\Omega$]')
plt.ylabel('Potencia [$W$]')
plt.title(r'Potencia en el transistor de paso \textbf{TIP42}')
plt.plot(RL, p3,color='darkorchid',label = 'Vo = 3.3V',linewidth=3)
plt.plot(RL, p5, color='#e377c2', label = 'Vo = 5V',linewidth=3)

plt.legend()
plt.savefig('graficos/potencia.png')
plt.show()