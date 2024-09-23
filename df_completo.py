import os
import pandas as pd
import re
import matplotlib.pyplot as plt


folder_path = 'C:\Taller python etsidi'  # Cambia esto a la ruta de tu carpeta

# Creamos el dataframe 'global' de febrero en este caso
df_feb = pd.DataFrame({})
# Recorre cada archivo en la carpeta
for file_name in os.listdir(folder_path):
    # Comprueba si el archivo tiene la extensión .xls
    if file_name.endswith('.xls'):
        file_path = os.path.join(folder_path, file_name)  # Crea la ruta completa
        # Lee el archivo con pandas
        df = pd.read_excel(file_name, usecols='B:C', skiprows=8, thousands='.', decimal=',')
        print(f"Archivo {file_name} leído correctamente.")
    
        def procesar_fechas_horas(x):
            patron_fecha = r'\b(?:\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4}|\d{4}[\/\-]\d{1,2}[\/\-]\d{1,2})\b'
            fechas_encontradas = re.findall(patron_fecha, x)
            fecha = fechas_encontradas[0]
            patron_horas = r'\b\d{2}\/\d{2}\/\d{4} (\d{2})\b'
            horas_encontradas = re.findall(patron_horas, x)
            hora = horas_encontradas[0] # + '-' + horas_encontradas[1]
            return fecha + ' ' + hora

        # Aplica la función procesar_fechas_horas a todas la celdas de la columna Dia
        df['Dia'] = df['Dia'].apply(procesar_fechas_horas)

        # Convertir la columna 'fecha' al tipo datetime
        df['Dia'] = pd.to_datetime(df['Dia'], format="%d/%m/%Y %H")

        # Asignar la columna 'Dia' como índice del DataFrame
        df.set_index('Dia', inplace=True)
        
        # print(df.head())
        df_feb = pd.concat([df_feb, df], axis=0)

print(df_feb.head())