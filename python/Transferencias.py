import numpy as np
import matplotlib.pyplot as plt


def procesarPuntos(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    z = datos_simul[:, 2]
    return x, y,z

def buscar_margen_fase(frecuencia, magnitud, fase):
    indices_cruce = np.where(np.diff(np.sign(magnitud)))[0]

    # Extraer la frecuencia y la fase en los puntos de cruce
    frec_cruce = frecuencia[indices_cruce]
    margen_fase = fase[indices_cruce]

    return frec_cruce, margen_fase


def graficarTransferencia(nombreArchivo, titulo,nombreImagen):
    freq,mag,fase = procesarPuntos(nombreArchivo)

    frec_cruce, margen_fase = buscar_margen_fase(freq, mag, fase)


    fig1, ax1 = plt.subplots()
    # plt.grid(True)

    ax1.set_xlabel('Frequencia [Hz]')
    ax1.set_xscale('log')
    ax1.set_xlim(10**1,10**9)
    ax1.grid(True, ls="--")
    # acomodar los ejes


    ax1.set_ylabel('Ganancia [dB]',color = 'darkorchid')
    plt.title(titulo)

    plot_1 = ax1.plot(freq, mag,color='darkorchid',linewidth=3)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Fase [°]',color = '#e377c2')
    plot_2 = ax2.plot(freq, fase,color='#e377c2' ,linewidth=1,linestyle='dashed')

    # for fc in frec_cruce:
    #     ax1.axvline(x=fc, color='r', linestyle='--', label='Cruce de 0 dB' if fc == frec_cruce[0] else "")

    ax2.axhline(y=0, color='gray', linestyle='--', linewidth=1)
    for fc, mf in zip(frec_cruce, margen_fase):


        ax2.plot([fc, fc], [0, mf], color='r', lw=1.5)
        ax2.text(fc-500, mf-20, f'{mf:.1f}°', color='r', fontsize=10, ha='right')

    lns = plot_1 + plot_2
    labels = [l.get_label() for l in lns]
    # plt.legend(lns, labels, loc=0)
    plt.tight_layout()
    plt.savefig(nombreImagen)

# para 5V
titulo = 'Respuesta en frecuencia para $V_O = 5V$ y $R_L= 10 \Omega$'
nombreImagen='graficos/TransferenciaLazoTensionSinCompensar5_RL10.png'
graficarTransferencia('resources/Sin-compensar/Vf5-Rl10.txt',titulo,nombreImagen)

titulo = 'Respuesta en frecuencia para $V_O = 5V$ y $R_L= 6,8 \Omega$'
nombreImagen='graficos/TransferenciaLazoCorrienteSinCompensar5_RL-68.png'
graficarTransferencia('resources/Sin-compensar/Vf5-Rl68.txt',titulo,nombreImagen)

titulo = 'Respuesta en frecuencia para $V_O = 5V$ y $R_L= 8 \Omega$'
nombreImagen='graficos/TransferenciaLazoTensionSinCompensar5_RL-8.png'
graficarTransferencia('resources/Sin-compensar/Vf5-Rl8.txt',titulo,nombreImagen)

# para 3.3V
titulo = 'Respuesta en frecuencia para $V_O = 3.3V$ y $R_L= 10 \Omega$'
nombreImagen='graficos/TransferenciaLazoTensionSinCompensar3_RL10.png'
graficarTransferencia('resources/Sin-compensar/Vf3-Rl10.txt',titulo,nombreImagen)

titulo = 'Respuesta en frecuencia para $V_O = 3.3V$ y $R_L= 6 \Omega$'
nombreImagen='graficos/TransferenciaLazoCorrienteSinCompensar3_RL-6.png'
graficarTransferencia('resources/Sin-compensar/Vf3-Rl6.txt',titulo,nombreImagen)

titulo = 'Respuesta en frecuencia para $V_O = 3.3V$ y $R_L= 4,4 \Omega$'
nombreImagen='graficos/TransferenciaLazoTensionSinCompensar3_RL-44.png'
graficarTransferencia('resources/Sin-compensar/Vf3-Rl44.txt',titulo,nombreImagen)


plt.show()