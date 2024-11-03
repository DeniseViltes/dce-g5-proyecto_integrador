import numpy as np
import os

def eliminar_archivo_si_existe(nombre_archivo):
    # Verificamos si el archivo existe y lo eliminamos
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
def guardar_variables_en_txt(nombre_archivo, variables):

    with open(nombre_archivo, 'a') as archivo:
        for nombre, valor in variables.items():
            archivo.write(f"{nombre}: {valor}\n")



def escribirComponentes(archivo):
    eliminar_archivo_si_existe(archivo)

    for i in range(0, N):
        cumple = False
        if C * Rcr[i] >= (1 / f) * 10:
            cumple = True

        resultados = {
            "Duty": D[i],
            "T": 1 / f,
            "ton": ton[i],
            "Is (minimo)": Is_min,
            "delta Il": deltaI_L,
            "L (critico)": Lcr[i],
            "R (critico)": Rcr[i],
            "C": C,
            "tau": Rcr[i] * C,
            "cumple": "Si" if cumple else "No"
        }
        guardar_variables_en_txt(archivo, resultados)

def L_critico(Rmax, D):
    L = (1 - D) * Rmax / (2 * f)
    return L

def R_critico(L, D):
    R = 2 * f * L / (1 - D)
    return R


critico = r"C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 4\ResultadoCuentitas.txt"

N = 1
Vs = 6.35
Vin = np.linspace(12,36,N)
f = 200*10**3
Vr = 0.15
Is_min = 0.1  #se supune que tengo que poner la minima aca, hay que ver como calculamos esto
Il_max = 2*Is_min
deltaI_L =Is_min/2


D = Vs/Vin

ton = D/f

toff = 1/f - ton



Rmax = Vs/Is_min

Lcr= L_critico(Rmax, D)
Rcr = R_critico(Lcr, D)


C = deltaI_L/(8*f*Vr)
# C=(1-D)*Vs/(8*(f**2)*Vr*Lcr)

escribirComponentes(critico)


operativo =r"C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 4\intento1.txt"


Is = 0.85
Rmax = Vs/Is
Lcr= L_critico(Rmax, D)
Lcr *=10
Rcr = R_critico(Lcr, D)


C *=10

escribirComponentes(operativo)


