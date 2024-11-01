
def guardar_variables_en_txt(nombre_archivo, variables):

    with open(nombre_archivo, 'w') as archivo:
        for nombre, valor in variables.items():
            archivo.write(f"{nombre}: {valor}\n")




Vs = 6.35
Vin = 12
f = 200*10**3
Vr = 0.18
Is_min = 0.2  #se supune que tengo que poner la minima aca, hay que ver como calculamos esto
Il_max = 2*Is_min


D = Vs/Vin

ton = D/f

toff = 1/f -ton



Rmax = Vs/Is_min

Lcr = (1-D)*Rmax/(2*f)
# Lcr = 1.25*Lcr

Rcr = 2*f*Lcr/(1-D)
# o.. elijo un Lcr y calculo Rcr?




# C = deltaI_L/(8*f*Vr)
C=(1-D)*Vs/(8*(f**2)*Vr*Lcr)


componentes = {
    "Duty": D,
    "T": 1/f,
    "ton": ton,
    "Is (minimo)": Is_min,
    "L (critico)": Lcr,
    "R (critico)": Rcr,
    "C" :C
}

guardar_variables_en_txt(r"C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 4\ComponentesSinRealimentar.txt", componentes)