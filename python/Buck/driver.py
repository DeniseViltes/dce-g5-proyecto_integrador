

Qg = 26*10**(-9)
Qrr = 0.85*10**(-9)

Iboot= 500*10**(-6)

fsw = 200*10**3

delta_V = 0.1

Cboot = (Qg +Qrr + Iboot/fsw)/delta_V

print(Cboot)