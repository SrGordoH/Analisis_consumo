import pandas as pd
import matplotlib.pyplot as plt

# archivo = "C:\Taller python etsidi\descarga01_02_2024_al_01_02_2024.xls"
df = pd.read_excel('Febrero_Completo.xlsx', thousands='.', decimal=',')

df['Dia'] = pd.to_datetime(df['Dia'], format='%Y-%m-%d %H:%M:%S')

# for fecha in df['Dia']:
#     es_fin_de_semana = fecha.dayofweek >= 5 # Devuelve True si es fin de semana y False si no lo es
#     df['Finde'] = es_fin_de_semana

df['Finde'] = df['Dia'].dt.dayofweek >= 5  # Forma más simple de ejecutar el bucle de arriba

df.set_index('Dia', inplace=True) ## Está por ver que sea lo mejor, es necesario para usar resample

# print(df.head())
# print(type(df.iloc[0].Dia))
df_diario = pd.DataFrame({})

df_diario['Total diario'] = df.resample('D').sum()['Consumo']
df_diario['Media horaria'] = df.resample('D').mean()['Consumo']
print(df_diario.head())

df['Media diaria'] = df.resample('D').mean()['Consumo']
df['Total diario'] = df.resample('D').sum()['Consumo']
# print(df.head())

# Media por horas el mes de febrero


## Consumo diario total    
# consumo_diario = df['Consumo'].sum()
# print("\n Consumo agregado por dia:")
# print(consumo_diario, 'Wh')

## Consumo medio por hora un dia especifico
# consumo_medio = df['Consumo'].mean()
# print("\n Consumo medio por día:")
# print(f'{consumo_medio:.3f} Wh')


# consumo_max = df['Consumo'].max()
# ## Tramo horario de máximo consumo
# indice_max = df['Consumo'].idxmax()
# # print(indice_max) # En indice máx es la hora

# print("\n Tramo horario (de 1 hora) de consumo máximo:")
# print(f'De {indice_max.hour}:00 a {indice_max.hour + 1}:00 h, con un consumo de {consumo_max} Wh')

# consumo_min = df['Consumo'].min()
# indice_min = df[df['Consumo'] == consumo_min].index # Filtra todos los índices donde el valor es igual al mínimo
# print(indice_min) 

# print("\n Tramo horario de consumo minimo:")
# print(f'De {indice_min[0].hour}:00 a {indice_min[-1].hour + 1}:00 h, con un consumo de {consumo_min} Wh')

# print(type(df.iloc[0].Consumo))
# print(df.head())
df_diario.plot()
plt.xlabel('Horas')
plt.ylabel('Consumo (Wh)')
plt.show()


