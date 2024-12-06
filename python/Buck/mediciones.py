import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
# from cargaDinamica import *

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





# RL5,Vo5,Io5=procesarPuntos('resources/stepRL5V.txt')
# RL3,Vo3,Io3=procesarPuntos('resources/stepRL3V.txt')
# RL,Vo_simu,Io=procesarPuntos('resources/mediciones/rectaCargaSimu.txt')
R_carga,Vo,Io=procesarPuntos('resources/mediciones/rectaCarga.txt')


# Rectas de carga


fig1, ax1 = plt.subplots()
plt.grid(True)

ax1.set_xlabel('RL [$\Omega$]')
ax1.set_ylabel('Tensión de salida[V]',color ='darkorchid')
plt.title('Recta de carga')


plot_1 = ax1.plot(R_carga, Vo, color='darkorchid', label = 'Tensión',linewidth=3)


ax2 = ax1.twinx()
ax2.set_ylabel('Corriente [A]',color = '#e377c2')
plot_2 = ax2.plot(R_carga, Io, color='#e377c2', label = 'Corriente',linewidth=3)

lns = plot_1 + plot_2
labels = [l.get_label() for l in lns]
plt.legend(lns, labels, loc=0)
plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\python\Buck\graficos\Recta_de_Carga.png')


# Rectas de linea

Vreg_medida, Vo_medida = procesarPuntos2VA('resources/mediciones/rectaLinea.txt')
# Vreg5, Vo5 = procesarPuntos2VA('resources/RtaLinea5.txt')




fig5 = plt.figure()
plt.grid(True)

plt.xlabel('Tensión de entrada [V]')
plt.ylabel('Tensión de salida[V]')
plt.title('Regulación de Linea ')
# plt.plot(Vreg5, Vo5,color='darkorchid',label = 'Simulación',linewidth=3)
plt.plot(Vreg_medida, Vo_medida, color='skyblue', label = 'Medición',linewidth=3)
# plt.xlim([3,10])
plt.legend()
plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\python\Buck\graficos\rectasDeLinea.png')





# duty

Vdd, duty = procesarPuntos2VA('resources/mediciones/duty.txt')

fig6 = plt.figure()
plt.grid(True)

plt.xlabel('Tensión de entrada [V]')
plt.ylabel('Duty Cicle')
plt.title('Duty Cicle vs Tensión de entrada ')
# plt.plot(Vreg5, Vo5,color='darkorchid',label = 'Simulación',linewidth=3)
plt.plot(Vdd,duty, color='darkorchid',linewidth=3)
# plt.xlim([3,10])
plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\python\Buck\graficos\Recta_de_linea.png')






# # Potencia
#
# RL5,Pl5,Ptip5=procesarPuntos('resources/mediciones/potencia5.txt')
# RL3,Pl3,Ptip3=procesarPuntos('resources/mediciones/potencia3.txt')
#
#
#
# rL3,p3 = procesarPuntos2VA('resources/potencia-vo3.txt')
# rL5,p5 = procesarPuntos2VA('resources/potencia-vo5.txt')
#
#
# pmaxRl5 = max(Ptip5)
#
# Rmax5= RL5[np.where(Ptip5 == pmaxRl5 )[0]]
# print('Rmax3=' ,Rmax5)
# print('Pmax=' , pmaxRl5)
#
#
# pmaxRl3 = max(Ptip3)
#
# Rmax3= RL3[np.where(Ptip3 == pmaxRl3 )[0]]
# print('Rmax5=' ,Rmax3)
# print('Pmax=' , pmaxRl3)
#
#
#
# fig6 = plt.figure()
# plt.grid(True)
#
# plt.xlabel('RL [$\Omega$]')
# plt.ylabel('Potencia [W]')
# plt.title('Potencia para Vo = 5V')
#
# plt.plot(RL5, Pl5, color='darkorchid', label = 'Medición en RL',linewidth=3)
# plt.plot(rL5, p5, color='#e377c2', label = 'Simulación en el TIP',linewidth=3)
# plt.plot(RL5, Ptip5, color='skyblue', label = 'Medición en el TIP',linewidth=3)
#
# plt.xlim([0,20])
#
# plt.legend()
# plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\graficos/potencia5.png')
#
#
# fig7 = plt.figure()
# plt.grid(True)
#
# plt.xlabel('RL [$\Omega$]')
# plt.ylabel('Potencia [W]')
# plt.title('Potencia para Vo = 3')
#
# plt.plot(RL3, Pl3, color='darkorchid', label = 'Medición en RL',linewidth=3)
# plt.plot(rL3, p3, color='#e377c2', label = 'Simulación en el TIP',linewidth=3)
# plt.plot(RL3, Ptip3, color='skyblue', label = 'Medición en el TIP',linewidth=3)
#
# plt.xlim([0,20])
#
# plt.legend()
# plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\graficos/potencia3.png')
#
#
#
# # Eficiencia
#
# # wl/(wl + wt)
#
# fig7 = plt.figure()
# plt.grid(True)
#
# plt.xlabel('RL [$\Omega$]')
# plt.ylabel('Potencia [W]')
# plt.title('Eficiencia')
#
# plt.plot(RL3, Pl3/(Pl3+Ptip3), color='darkorchid', label = 'Vo = 3,3V',linewidth=3)
# plt.plot(RL5, Pl5/(Pl5+Ptip5), color='skyblue', label = 'Vo = 5 V',linewidth=3)
# #
#
# plt.xlim([0,20])
#
# plt.legend()
# plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\graficos/eficienca.png')
#
#
#
#
# # # Carga dinamica
# #
# # Vd3,Vo3=procesarPuntos2VA('resources/mediciones/cargadinamica3.txt')
# # Vd5,Vo5=procesarPuntos2VA('resources/mediciones/cargadinamica5.txt')
# #
# # tiempo =np.linspace(0, 0.01, len(Vd3))
# #
# # fig8 = plt.figure()
# # plt.grid(True)
# #
# # plt.xlabel('tiempo')
# # plt.ylabel('Tensión de salida [V]')
# # plt.title('Carga dinamica')
# #
# # window_size = 100
# #
# # def moving_average(data, window_size):
# #     return np.convolve(data, np.ones(window_size) / window_size, mode='valid')
# #
# #
# # vo3 = moving_average(Vo3, len(Vo3))
# # t= tiempo[:len(vo3)]
# #
# #
# # plt.plot(t, vo3/1000,color='darkorchid',label = 'Vo = 3V',linewidth=3)
# # # plt.plot(tiempo, Vd3/1000,color='darkorchid',label = 'Vo = 3V',linewidth=3)
# # # plt.plot(Vd5/1000, Vo5/100,color='darkorchid',label = 'Vo = 5V',linewidth=3)



# Vo3_medicion,Io3_medicion=procesarPuntos2VA('resources/mediciones/folback-3,3-nuevo.txt')
#
#
# fig3 = plt.figure()
# plt.grid(True)
#
# plt.xlabel('$I_{RL}$ [mA]')
# plt.ylabel('Tensión de salida [V]')
# plt.title('Foldback para Vo = 3,3V')
# plt.plot(Io3*10**3,Vo3,color='darkorchid',label = 'Simulación',linewidth=3)
# plt.plot(Io3_medicion,Vo3_medicion,color='#cd7584',label = 'Medición',linewidth=3)
#
# plt.axvline(x=750, color='r', linestyle='--')
# plt.text(740,2, '$750 mA$', color='r', fontsize=10, ha='right')
#
# plt.axvline(x=200, color='r', linestyle='--')
# plt.text(270,2, '$200 mA$', color='r', fontsize=10, ha='right')
#
# plt.legend()
#
# plt.savefig(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\graficos/Foldback3nuevo.png')
#
#


plt.show()