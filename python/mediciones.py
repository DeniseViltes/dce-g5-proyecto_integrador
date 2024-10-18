import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    z = datos_simul[:, 2]
    return x, y,z


def procesarPuntos2VA(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    return x, y

Vreg_medida, Vo_medida = procesarPuntos2VA('resources/mediciones/regulación-de-linea.txt')
Vreg, Vo = procesarPuntos2VA('resources/RtaLinea3.txt')



RL5,Vo5,Io5=procesarPuntos('resources/stepRL5V.txt')
RL3,Vo3,Io3=procesarPuntos('resources/stepRL3V.txt')
RL5_medicion,Vo5_medicion,Io5_medicion=procesarPuntos('resources/mediciones/foldback-5.txt')
RL3_medicion,Vo3_medicion,Io3_medicion=procesarPuntos('resources/mediciones/foldback-3,3.txt')

fig1 = plt.figure()
plt.grid(True)

plt.xlabel('RL [$\Omega$]')
plt.ylabel('Tensión de salida[V]')
plt.title('Rectas de carga para Vo = 5V')

plt.xlim([0,15])
plt.plot(RL5, Vo5, color='darkorchid', label = 'Simulación',linewidth=3)
plt.plot(RL5_medicion, Vo5_medicion, color='skyblue', label = 'Medición',linewidth=3)


plt.axvline(x=6.8, color='#e377c2', linestyle='--')
plt.text(8,2, '$6,8 \Omega$', color='r', fontsize=10, ha='right')
plt.legend()
plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\graficos/rectasDeCarga5V.png')


fig2 = plt.figure()
plt.grid(True)

plt.xlabel('RL [$\Omega$]')
plt.ylabel('Tensión de salida[V]')
plt.title('Rectas de carga para Vo = 3,3V')
plt.xlim([0,15])
plt.plot(RL3, Vo3, color='darkorchid', label = 'Simulación',linewidth=3)
plt.plot(RL3_medicion, Vo3_medicion, color='skyblue', label = 'Medición',linewidth=3)


plt.axvline(x=4.4, color='darkorchid', linestyle='--')
plt.text(5.3,2, '$4,4 \Omega$', color='r', fontsize=10, ha='right')

plt.legend()
plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\graficos/rectasDeCarga3V.png')


fig3 = plt.figure()
plt.grid(True)

plt.xlabel('$I_{RL}$ [mA]')
plt.ylabel('Tensión de salida [V]')
plt.title('Foldback para Vo = 3,3V')
plt.plot(Io3*10**3,Vo3,color='darkorchid',label = 'Simulación',linewidth=3)
plt.plot(Io3_medicion,Vo3_medicion,color='skyblue',label = 'Medición',linewidth=3)

plt.axvline(x=750, color='r', linestyle='--')
plt.text(740,2, '$750 mA$', color='r', fontsize=10, ha='right')

plt.axvline(x=200, color='r', linestyle='--')
plt.text(260,2, '$200 mA$', color='r', fontsize=10, ha='right')

plt.legend()

plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\graficos/Foldback3.png')

fig4 = plt.figure()
plt.grid(True)

plt.xlabel('$I_{RL}$ [mA]')
plt.ylabel('Tensión de salida [V]')
plt.title('Foldback para Vo = 5V')
plt.plot(Io5*10**3,Vo5,color='darkorchid',label = 'Simulación',linewidth=3)
plt.plot(Io5_medicion,Vo5_medicion,color='skyblue',label = 'Medición',linewidth=3)

plt.axvline(x=750, color='r', linestyle='--')
plt.text(740,2, '$750 mA$', color='r', fontsize=10, ha='right')

plt.axvline(x=200, color='r', linestyle='--')
plt.text(260,2, '$200 mA$', color='r', fontsize=10, ha='right')

plt.legend()

plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\graficos/Foldback5.png')



fig5 = plt.figure()
plt.grid(True)

plt.xlabel('Tensión de entrada [V]')
plt.ylabel('Tensión de salida[V]')
plt.title('Rectas de Linea')
plt.plot(Vreg, Vo,color='darkorchid',label = 'Simulación',linewidth=3)
plt.plot(Vreg_medida, Vo_medida, color='skyblue', label = 'Medición',linewidth=3)

plt.legend()
plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\graficos/rectasDeLinea.png')




plt.show()