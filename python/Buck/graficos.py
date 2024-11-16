import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True


def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    return x, y

def procesarPuntos_5VA(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    a = datos_simul[:, 0]
    b = datos_simul[:, 1]
    c = datos_simul[:, 2]
    d = datos_simul[:, 3]
    e = datos_simul[:, 4]
    return a,b,c,d,e

#Support
t,Vbat_neg, Vposa_neg, Venable,Vref = procesarPuntos_5VA(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 4\Simus\resultados-simus\support.txt')



fig1 = plt.figure()
plt.grid(True)


ticks_y = np.arange(-14, 15, 2)
plt.yticks(ticks_y)

t *= 1000
plt.xlabel('Tiempo [ms]')
plt.ylabel('Tensión de salida [V]')
plt.title(r'Tensiones disponibles en la salida del bloque \textit{support}')
plt.plot(t, Vbat_neg,color='darkorchid',label = '$-V_{bat}$',linewidth=3)
plt.plot(t, Vposa_neg, color='#e377c2', label = '$-V_{posa}$',linewidth=3)
plt.plot(t,Venable, color='crimson', label = '$V_{enable}$',linewidth=3)
plt.plot(t,Vref, color='orchid', label = '$V_{ref}$',linewidth=3)

plt.legend()
plt.savefig('graficos/support.png')





t1,Vo12 = procesarPuntos(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 4\Simus\resultados-simus\Buck-Vo_Vin-12V.txt')
t2,Vo36 = procesarPuntos(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 4\Simus\resultados-simus\Buck-Vo_Vin-36V.txt')
tl,L = procesarPuntos(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 4\Simus\resultados-simus\Buck-L_Vin-12V.txt')


fig3 = plt.figure()
plt.grid(True)




plt.xlabel('Tiempo [ms]')
plt.ylabel('Tensión de salida [V]')
plt.title('Tensión de salida del bloque buck')
plt.plot(t1*1000, Vo12,color='darkorchid',label = '$V_{in} = 12V$',linewidth=3)
plt.plot(t2*1000, Vo36, color='#e377c2', label = '$V_{in} = 36V$',linewidth=3)
plt.axhline(y = 6.35,color = "deepskyblue",linestyle='--', linewidth=2,label = "6,35 V")

plt.legend()
plt.savefig('graficos/salidas_buck.png')

fig4 = plt.figure()
plt.grid(True)




plt.xlabel('Tiempo [ms]')
plt.ylabel('Corriente [mA]')
plt.title('Corriente en el inductor')
plt.plot(tl*1000, L*1000,color='darkorchid',linewidth=3)
plt.axhline(y = 20,color = "deepskyblue",linestyle='--', linewidth=2,label = "20 mA")

plt.savefig('graficos/corriente_buck.png')

fig5 = plt.figure()
plt.grid(True)



t *= 1000
plt.xlabel('Tiempo [ms]')
plt.ylabel('Corriente [mA]')
plt.title('Corriente luego de estabilizar en el inductor')
plt.plot(tl*1000, L*1000,color='darkorchid',linewidth=3)
plt.axhline(y = 20,color = "deepskyblue",linestyle='--', linewidth=2,label = "20 mA")

plt.xlim([0.25,0.35])
plt.savefig('graficos/corriente_buck_zoom.png')


fig = plt.figure()
plt.grid(True)

plt.xlabel('Tiempo [ms]')
plt.ylabel('Tensión de salida [V]')
plt.title('Tensión de salida del bloque buck')
plt.plot(t1*1000, Vo12,color='darkorchid',label = '$V_{in} = 12V$',linewidth=3)
plt.plot(t2*1000, Vo36, color='#e377c2', label = '$V_{in} = 36V$',linewidth=3)
plt.axhline(y = 6.35,color = "deepskyblue",linestyle='--', linewidth=2,label = "6,35 V")

plt.legend()
plt.xlim([0.35,0.4])
plt.ylim([6,6.5])
plt.savefig('graficos/salidas_buck_zoom.png')


plt.show()
