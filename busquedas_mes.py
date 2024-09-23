import pandas as pd

def hora_mayor_consumo(df, dia):
    # Filtramos el dataframe por el día que nos interesa
    df_dia = df[df.index.date == dia]
    # Encontramos el índice (hora) de mayor consumo
    idx_max = df_dia['Consumo'].idxmax()
    # Obtenemos la fila completa
    fila_mayor_consumo = df_dia.loc[idx_max]
    # Extraemos la hora y el consumo
    hora = idx_max.time()  # Extraemos solo la hora
    consumo = fila_mayor_consumo['Consumo']
    return hora, consumo

def hora_menor_consumo(df, dia):  # Hay que mejorarlo porque hay dias con tramos de varias horas que es 0 y no se refleja
    df_dia = df[df.index.date == dia]
    df_dia_sin_cero = df_dia[df_dia['Consumo'] > 0]
    if df_dia_sin_cero.empty:
        return None, None  # No hay consumos mayores que 0
    idx_min = df_dia_sin_cero['Consumo'].idxmin()
    fila_menor_consumo = df_dia_sin_cero.loc[idx_min]
    hora = idx_min.time()  # Extraemos solo la hora
    consumo = fila_menor_consumo['Consumo']      
    return hora, consumo

def tramos_consumo_cero(df, dia):
    # Filtrar el dataframe para obtener solo el día que nos interesa
    df_dia = df[df.index.date == dia]
    
    # Filtrar las filas donde el consumo es 0
    df_cero = df_dia[df_dia['Consumo'] == 0]
    
    if df_cero.empty:
        return None, None  # No hay tramos de consumo cero
    
    # Encontrar tramos consecutivos de horas donde el consumo es 0
    tramos = []
    inicio = df_cero.index[0]  # Primera hora de consumo cero
    fin = inicio
    
    for i in range(1, len(df_cero)):
        # Si la hora actual es consecutiva a la anterior
        if df_cero.index[i] == df_cero.index[i - 1] + pd.Timedelta(hours=1):
            fin = df_cero.index[i]  # Actualizar el final del tramo
        else:
            # Guardar el tramo actual y empezar un nuevo tramo
            tramos.append((inicio.time(), fin.time()))
            inicio = df_cero.index[i]
            fin = inicio
    
    # Añadir el último tramo
    tramos.append((inicio.time(), fin.time()))
    
    return tramos


def dia_mayor_consumo(df):
    df_por_dia = df.resample('D').sum()
    idx_max = df_por_dia['Consumo'].idxmax()
    fecha = idx_max.date() 
    fila_max_agregado = df_por_dia.loc[idx_max]
    consumo = fila_max_agregado['Consumo']
    if fila_max_agregado['Finde']:
        finde = 'era fin de semana'
    else:
        finde = 'no era fin de semana'
    return fecha, consumo, finde

def dia_menor_consumo(df):
    df_por_dia = df.resample('D').sum()
    idx_min = df_por_dia['Consumo'].idxmin()
    fecha = idx_min.date() 
    fila_min_agregado = df_por_dia.loc[idx_min]
    consumo = fila_min_agregado['Consumo']
    if fila_min_agregado['Finde']:
        finde = 'era fin de semana'
    else:
        finde = 'no era fin de semana'
    return fecha, consumo, finde
    
def consumo_promedio_por_dia(df):
    return df.resample('D').mean()['Consumo']

def consumo_semana_vs_finde(df):
    consumo_semana = df[~df['Finde']]['Consumo'].sum()
    consumo_finde = df[df['Finde']]['Consumo'].sum()
    comparativa = {'Consumo Semana': consumo_semana, 'Consumo Finde': consumo_finde}
    return comparativa

def dia_mayor_horas_consumo_umbral(df, umbral):
    df_bajo_consumo = df[df['Consumo'] < umbral]
    horas_por_dia = df_bajo_consumo.resample('D').size()
    return horas_por_dia.idxmax(), horas_por_dia.max()

def hora_mayor_consumo_finde(df):
    df_finde = df[df['Finde']]
    return df_finde.loc[df_finde['Consumo'].idxmax()]


df = pd.read_excel('Febrero_Completo.xlsx', thousands='.', decimal=',')

df['Dia'] = pd.to_datetime(df['Dia'], format='%Y-%m-%d %H:%M:%S')

df['Finde'] = df['Dia'].dt.dayofweek >= 5  

df.set_index('Dia', inplace=True)

print(df.iloc[0].index)

# Hora de mayor consumo en un dia específico
dia_especifico = pd.Timestamp('2024-02-06').date()  # Día que se desea buscar
# print(dia_especifico)
hora, consumo = hora_mayor_consumo(df, dia_especifico)
print(f"Para el dia {dia_especifico}, el tramo horario de mayor consumo fue de las {hora.hour} a las {hora.hour+1} h, con un consumo de {consumo} Wh")

# Hora de menor consumo en un dia específico
# dia_especifico = pd.Timestamp('2024-02-02').date()  # Día que se desea buscar
# hora_ini, hora_fin, consumo = hora_menor_consumo(df, dia_especifico)
# print(f"Para el dia {dia_especifico}, el tramo horario de menor consumo fue de las {hora_ini} a las {hora_fin} h, con un consumo de {consumo} Wh")

# Dia de consumo máximo en el mes
fecha, consumo, fnde = dia_mayor_consumo(df)
# dia_fromateado = dia.strftime("%#d de %B de %Y")
print(f"El dia de mayor consumo en el mes de febrero fue el {fecha.day} con un consumo de {consumo} Wh y", fnde)

# Dia de consumo máximo en el mes
fecha, consumo, fnde = dia_menor_consumo(df)
print(f"El dia de menor consumo en el mes de febrero fue el {fecha.day} con un consumo de {consumo} Wh y", fnde)

# Lista con el consumo promedio horario por dia
# consumo_promedio = consumo_promedio_por_dia(df)
# print(consumo_promedio)

# Comparativa finde vs entre semana
comparativa = consumo_semana_vs_finde(df)
print('En el mes de febrero el consumo entre semana fue de', comparativa["Consumo Semana"], 'Wh mientras que el finde fue de', comparativa['Consumo Finde'],'Wh')

horas, consumo = dia_mayor_horas_consumo_umbral(df, 500)
print(horas, consumo)