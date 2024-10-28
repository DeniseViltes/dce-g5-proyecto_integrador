import pandas as pd

df = pd.read_excel(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\potencia3.xlsx')


df.to_csv('resources/mediciones/potencia3.txt', sep='\t', index=False)

