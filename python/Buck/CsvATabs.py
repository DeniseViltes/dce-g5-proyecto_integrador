import pandas as pd

df = pd.read_excel(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\python\Buck\resources\rtaFreq.xlsx')


df.to_csv('resources/mediciones/rtaEnFreqInductor.txt', sep='\t', index=False)

