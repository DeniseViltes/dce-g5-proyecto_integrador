import numpy as np
from sympy.utilities.codegen import InOutArgument

Vout = 6.35

Vin = 21 # Minimo

Vf=1
Vsat=1

f= 200*10**3

t_On_Off = (Vout +Vf) / (Vin-Vsat-Vout)  # ton/toff

sum_On_Off = 1/f

toff = (ton0 +toff0)/(ton0/toff0+1)

ton= sum_On_Off-toff

Ct = 4.0*10**(-5)*ton

Ipk = 2*Iout

Rsc = 0.3/Ipk

L = (Vin -Vsat -Vout)/ Ipk *ton

Co = Ipk * sum_On_Off/ (8*Vripple)
