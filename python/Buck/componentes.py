def guardar_variables_en_txt(nombre_archivo, variables):
    """
    Guarda las variables en un archivo de texto.

    Args:
    nombre_archivo (str): Nombre del archivo de salida, ej. "variables.txt".
    variables (dict): Diccionario con nombres y valores de variables.

    Ejemplo:
    variables = {"var1": 10, "var2": 3.14, "var3": "texto"}
    guardar_variables_en_txt("mi_archivo.txt", variables)
    """
    with open(nombre_archivo, 'w') as archivo:
        for nombre, valor in variables.items():
            archivo.write(f"{nombre}: {valor}\n")


Vout = 6.35

Vin = 12 # Minimo

Vf=0.5
Vsat=0
Iout= 1.6
f= 33*10**3
Vripple = 0.2

t_On_Off = (Vout +Vf) / (Vin-Vsat-Vout)  # ton/toff

sum_On_Off = 1/f

toff = sum_On_Off/(t_On_Off+1)

ton= sum_On_Off-toff

Ct = 4.0*10**(-5)*ton

Ipk = 2*Iout

Rsc = 0.3/Ipk

L = (Vin -Vsat -Vout)/ Ipk *ton

Co = Ipk * sum_On_Off/ (8*Vripple)


componentes = {
    "ton/toff": t_On_Off,
    "ton + toff": sum_On_Off,
    "toff": toff,
    "ton": ton,
    "Ct": Ct,
    "Ipk (switch)": Ipk,
    "Rs": Rsc,
    "L (min)": L,
    "Co": Co,
    "Duty": ton/sum_On_Off
}

# Ejemplo de uso
guardar_variables_en_txt(r"C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 4\ecuacionesComponentes.txt", componentes)