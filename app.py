# importar librerias
from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Leer los datos del archivo CSV
ruta_csv = Path(
    'C:/Users/Usuario/OneDrive/Desktop/TripleTen/APPs/Sprint7_LAST') / 'vehicles_us_mod.csv'
vehicles_us = pd.read_csv('vehicles_us_mod.csv')

# Crea un encabezado
st.header('Gráficos: Anuncios de venta de coches')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=vehicles_us['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# Crear una casilla de verificación
build_dispersion = st.checkbox('Gráfico de dispersión')

if build_dispersion:  # si la casilla de verificación está seleccionada
    st.write(
        'Construir un gráfico de dispersión identificar la relación odómetro vs precio')

    # Crear un scatter plot utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de scatter
    fig2 = go.Figure(data=[go.Scatter(
        x=vehicles_us['odometer'], y=vehicles_us['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig2.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig2, use_container_width=True)
