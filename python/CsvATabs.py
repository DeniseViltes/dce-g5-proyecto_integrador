import pandas as pd

df = pd.read_excel(r'C:\Users\---\Desktop\DCE\dce-g5-proyecto_integrador\Checkpoint 3\regDeLinea.xlsx')


df.to_csv('resources/mediciones/regulación-de-linea.txt', sep='\t', index=False)


# print(df.to_csv(sep='\t', index=False))
