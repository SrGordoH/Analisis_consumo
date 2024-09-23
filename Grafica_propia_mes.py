import streamlit as st
import pandas as pd
import plotly.express as px
import re

df = pd.read_excel('Febrero_Completo.xlsx', thousands='.', decimal=',')

df['Dia'] = pd.to_datetime(df['Dia'], format='%Y-%m-%d %H:%M:%S')


# Título de la aplicación
# st.title("Gráfica de un DataFrame usando Streamlit")

# # Mostrar el DataFrame
# st.write("Este es el DataFrame:")
# st.dataframe(df)

# Crear una gráfica usando Plotly Express
# fig = px.line(df, x='Dia', y='Consumo', title='Datos de horas y consumo de febrero')

# Mostrar la gráfica
# st.plotly_chart(fig)


# Filtrar el DataFrame para los datos de febrero 2024
# df = df[df['Fecha'].dt.month == 2]

# Extraer solo la parte de la fecha (sin hora) para poder filtrar por día
df['Fecha'] = df['Dia'].dt.date  # Dia se considera a el dato con fecha y hora

# Obtener lista de días únicos
dias_unicos = df['Fecha'].unique()

# Título de la aplicación
st.title("Gráficas de cada día en febrero 2024")

# Crear una gráfica por cada día
for dia in dias_unicos:
    # Filtrar los datos del día específico
    df_fecha = df[df['Fecha'] == dia]
    # print(df_fecha.head())
    # Crear la gráfica para ese día
    fig = px.bar(df_fecha, x='Dia', y='Consumo', title=f'Valores del {dia}')
    
    # Añadir etiquetas de valores en las barras
    fig.update_traces(text=df_fecha['Consumo'], textposition='outside')

    # Personalizar el título, los ejes y el estilo
    fig.update_layout(
        title_text='Valores por Fecha', 
        title_x=0.3,  # Centrar el título
        title_font=dict(size=24, color='darkblue'),
        xaxis_title='Fecha',
        yaxis_title='Consumo',
        xaxis_tickangle=-45,  # Rotar etiquetas del eje x
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Fondo transparente
        paper_bgcolor='white'  # Fondo del área de la gráfica
    ) # Mejorar, es feo

    # Mostrar la gráfica para ese día
    st.plotly_chart(fig)


## Para ejecutar el código
# C:\Users\hecto>cd C:\Prueba streamlit   #Carpeta donde esté el archivo que queremos ejecutar

# C:\Prueba streamlit>python -m streamlit run Grafica_propia_mes.py   # nombre del archivo

# To stop the Streamlit server, press `Ctrl+C` in the terminal.