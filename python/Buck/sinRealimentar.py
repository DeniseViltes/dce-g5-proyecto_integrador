
def guardar_variables_en_txt(nombre_archivo, variables):

    with open(nombre_archivo, 'w') as archivo:
        for nombre, valor in variables.items():
            archivo.write(f"{nombre}: {valor}\n")




Vout = 6.35
Vin = 12
Iout = 0.2  #se supune que tengo que poner la minima aca, hay que ver como calculamos esto
f = 200*10**3
Vr = 0.18
deltaI_L = 0.1


D = Vout/Vin

ton = D/f

toff = 1/f -ton



Rmax = 5

Lcr = (1-D)*Rmax/(2*f)


# o.. elijo un Lcr y calculo Rcr?




C = deltaI_L/(8*f*Vr)


componentes = {
    "Iout": Iout,
    "Duty": D,
    "T": 1/f,
    "ton": ton,
    "Rmax": Rmax,
    "L (critico)": Lcr,
    "C" :C
}

guardar_variables_en_txt(r"C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 4\ComponentesSinRealimentar.txt", componentes)