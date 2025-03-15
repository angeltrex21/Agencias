import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Definición de las rutas de los archivos
ruta_archivo_1 = 'C:/Users/jacin/OneDrive/Documentos/base de datos de escuela/INVESCOBEDO.txt'
ruta_archivo_2 = 'C:/Users/jacin/OneDrive/Documentos/base de datos de escuela/INVAPODACA.txt'
ruta_archivo_3 = 'C:/Users/jacin/OneDrive/Documentos/base de datos de escuela/INVMONTERREY.txt'
ruta_archivo_4 = 'C:/Users/jacin/OneDrive/Documentos/base de datos de escuela/INVSANNICOLAS.txt'

# Creación de los DataFrames utilizando las rutas definidas
df_1 = pd.read_csv(ruta_archivo_1, delimiter='|')  
df_2 = pd.read_csv(ruta_archivo_2, delimiter='|')  
df_3 = pd.read_csv(ruta_archivo_3, delimiter='|')
df_4 = pd.read_csv(ruta_archivo_4, delimiter='|')

# Concatenación de los DataFrames en uno solo
df_completo = pd.concat([df_1, df_2, df_3, df_4], ignore_index=True)

jupyter notebook list
