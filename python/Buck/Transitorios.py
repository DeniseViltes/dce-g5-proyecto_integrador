import numpy as np
import matplotlib.pyplot as plt

def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    return x, y


tiempo, vo_vin12_R_330 = procesarPuntos('resources/vo-vin12_R-330.txt')
tiempo1, vo_vin12_R_20 = procesarPuntos('resources/vo-vin12_R-20.txt')
tiempo2, vo_vin12_R_10 = procesarPuntos('resources/vo-vin12_R-10.txt')
tiempo3, vo_vin12_R_4 = procesarPuntos('resources/vo-vin12_R-4.txt')
tiempo4, transitorioLazoCerrado = procesarPuntos('resources/Buck-lazo-cerrado2.txt')


fig = plt.figure()
plt.grid(True)

plt.xlabel('Tiempo [m s]')
plt.ylabel('Tensión [V]',color = 'darkorchid')
plt.title('Respuesta temporal del lazo cerrado, PWM + BUCK')

plt.plot(tiempo4*10**3, transitorioLazoCerrado,color='darkorchid' ,linewidth=3)


plt.savefig('graficos/Transitorios.png')







fig1 = plt.figure()
plt.grid(True)

plt.xlabel('Tiempo [m s]')
plt.ylabel('Tensión [V]',color = 'darkorchid')
plt.title('Respuesta temporal del lazo cerrado $V_{in}=12V$')

plt.plot(tiempo*10**3, vo_vin12_R_330,color='darkorchid',label = '$R_{load}= 330\Omega$' ,linewidth=3)
plt.plot(tiempo1*10**3, vo_vin12_R_20,color='hotpink',label = '$R_{load}= 20\Omega$' ,linewidth=3)
plt.plot(tiempo2*10**3, vo_vin12_R_10,color='crimson',label = '$R_{load}= 10\Omega$' ,linewidth=3)
plt.plot(tiempo3*10**3, vo_vin12_R_4,color='indigo',label = '$R_{load}= 4\Omega$' ,linewidth=3)

plt.xlim([0,1])

plt.savefig('graficos/TransitoriosGananciaTension-Vin_12.png')

tiempo0, vo_vin12_R_330_SC = procesarPuntos('resources/vo-vin12_R-330-SINCOMPENSAR.txt')

fig3 = plt.figure()
plt.grid(True)

plt.xlabel('Tiempo [m s]')
plt.ylabel('Tensión [V]',color = 'darkorchid')
plt.title('Respuesta temporal del lazo cerrado $V_{in}=12V$')

plt.plot(tiempo*10**3, vo_vin12_R_330,color='darkorchid',label = 'Compensado' ,linewidth=3)
plt.plot(tiempo0*10**3,vo_vin12_R_330_SC,color='hotpink',label = 'Sin Compensar' ,linewidth=3)


plt.legend(loc='best')

plt.savefig('graficos/comparacinTransitorioAntesYDespues.png')




tiempo, vo_vin36_R_330 = procesarPuntos('resources/vo-vin36_R-330.txt')
tiempo1, vo_vin36_R_20 = procesarPuntos('resources/vo-vin36_R-20.txt')
tiempo2, vo_vin36_R_10 = procesarPuntos('resources/vo-vin36_R-10.txt')
tiempo3, vo_vin36_R_4 = procesarPuntos('resources/vo-vin36_R-4.txt')


fig2 = plt.figure()
plt.grid(True)

plt.xlabel('Tiempo [m s]')
plt.ylabel('Tensión [V]',color = 'darkorchid')
plt.title('Respuesta temporal del lazo cerrado $V_{in}=36V$')

plt.plot(tiempo*10**3, vo_vin36_R_330,color='darkorchid',label = '$R_{load}= 330\Omega$' ,linewidth=3)
plt.plot(tiempo1*10**3, vo_vin36_R_20,color='hotpink',label = '$R_{load}= 20\Omega$' ,linewidth=3)
plt.plot(tiempo2*10**3, vo_vin36_R_10,color='crimson',label = '$R_{load}= 10\Omega$' ,linewidth=3)
plt.plot(tiempo3*10**3, vo_vin36_R_4,color='indigo',label = '$R_{load}= 4\Omega$' ,linewidth=3)
plt.xlim([0,1])
plt.savefig('graficos/TransitoriosGananciaTension-Vin_36.png')
plt.show()

