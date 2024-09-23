import os
import pandas as pd

folder_path = 'C:\Taller python etsidi'  # Cambia esto a la ruta de tu carpeta

# Recorre cada archivo en la carpeta
for file_name in os.listdir(folder_path):
    # Comprueba si el archivo tiene la extensión .xls
    if file_name.endswith('.xls'):
        file_path = os.path.join(folder_path, file_name)  # Crea la ruta completa
        # Lee el archivo con pandas
        df = pd.read_excel(file_path)
        print(f"Archivo {file_name} leído correctamente.")
        # Aquí puedes trabajar con cada DataFrame 'df' como desees
