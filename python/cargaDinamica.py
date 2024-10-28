import numpy as np



def Promediar(vo):
    # Parámetros de la señal
    sampling_rate = 1000  # Frecuencia de muestreo en Hz
    signal_freq = 5       # Frecuencia de la señal en Hz
    duration = 2          # Duración de la adquisición en segundos
    amplitude = 1         # Amplitud de la señal
    window_size = 50      # Tamaño de la ventana de promedio

    # Tiempo de muestreo
    t = np.linspace(0, duration, len(vo), endpoint=False)

    # Generar una señal senoidal con ruido
    # noise = np.random.normal(0, 0.1, t.shape)  # Ruido aleatorio
    # signal = amplitude * np.sin(2 * np.pi * signal_freq * t) + noise

    # Función para calcular el promedio móvil
    def moving_average(vo, window_size):
        return np.convolve(vo, np.ones(window_size) / window_size, mode='valid')

    # Calcular el promedio móvil
    averaged_signal = moving_average(vo, window_size)

    # Tiempo ajustado para la señal promediada (se pierde una parte del borde)
    t_avg = t[:len(averaged_signal)]

    # Aquí tienes 'averaged_signal' que es la señal promediada
    # Y 't_avg' que es el tiempo correspondiente a la señal promediada
    return t_avg, averaged_signal

