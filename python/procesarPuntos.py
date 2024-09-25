import numpy as np

def procesarPuntos(nombreArchivo):

    datos_simul = np.genfromtxt('resources/TL1_A_1_a.txt', delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]

    return x, y
