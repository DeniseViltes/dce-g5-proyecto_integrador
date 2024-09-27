import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True



def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    z = datos_simul[:, 2]
    return x, y,z

RL5,Vo5,Io5=procesarPuntos('resources/Sin-compensar/stepRL5V.txt')
RL3,Vo3,Io3=procesarPuntos('resources/Sin-compensar/stepRL3V.txt')

fig1 = plt.figure()
plt.grid(True)

plt.xlabel('RL [$\Omega$]')
plt.ylabel('Tensión de salida[V]')
plt.title('Rectas de carga')
plt.plot(RL3, Vo3,color='darkorchid',label = 'Vo = 3.3V',linewidth=3)
plt.plot(RL5, Vo5, color='#e377c2', label = 'Vo = 5V',linewidth=3)

plt.axvline(x=4.4, color='darkorchid', linestyle='--')
plt.text(5.3,2, '$4,4 \Omega$', color='r', fontsize=10, ha='right')
plt.axvline(x=6.8, color='#e377c2', linestyle='--')
plt.text(8,2, '$6,8 \Omega$', color='r', fontsize=10, ha='right')

plt.legend()
plt.savefig('graficos/rectasDeCarga.png')


fig2 = plt.figure()
plt.grid(True)

plt.xlabel('$I_{RL}$ [mA]')
plt.ylabel('Tensión de salida [V]')
plt.title('Foldback')
plt.plot(Io3*10**3,Vo3,color='darkorchid',label = 'Vo = 3.3V',linewidth=3)
plt.plot(Io5*10**3, Vo5, color='#e377c2', label = 'Vo = 5V',linewidth=3)

plt.axvline(x=750, color='r', linestyle='--')
plt.text(740,2, '$750 mA$', color='r', fontsize=10, ha='right')
plt.axvline(x=200, color='r', linestyle='--')
plt.text(260,2, '$200 mA$', color='r', fontsize=10, ha='right')

plt.legend()
plt.savefig('graficos/Foldback.png')


RL,Vo5,Io5=procesarPuntos('resources/stepRL5V.txt')
RL,Vo3,Io3=procesarPuntos('resources/stepRL3V.txt')

fig2 = plt.figure()
plt.grid(True)

plt.xlabel('$I_{RL}$ [mA]')
plt.ylabel('Tensión de salida [V]')
plt.title('Foldback Compensado')
plt.plot(Io3*10**3,Vo3,color='darkorchid',label = 'Vo = 3.3V',linewidth=3)
plt.plot(Io5*10**3, Vo5, color='#e377c2', label = 'Vo = 5 V',linewidth=3)


plt.axvline(x=750, color='r', linestyle='--')
plt.text(740,2, '$750 mA$', color='r', fontsize=10, ha='right')

plt.axvline(x=200, color='r', linestyle='--')
plt.text(260,2, '$200 mA$', color='r', fontsize=10, ha='right')

plt.legend()
plt.savefig('graficos/FoldbacksCompensados.png')



plt.show()

