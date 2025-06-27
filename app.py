# Streamlit app

# importar librerías
import plotly_express as px
import streamlit as st
import pandas as pd

# carga y limpieza de datos
df = pd.read_csv("notebooks/vehicles_us.csv")
car_data = df.dropna(subset=['odometer']).copy()

# Título y descripción
st.header("Análisis de anuncios de venta de autos")
st.write("Elige el modo de interacción y genera los gráficos deseados.")

# Modo de interacción
mode = st.radio(
    "Selecciona cómo quieres generar los gráficos:",
    ('Botones', 'Casillas')
)


# Crear gráficos con botones
if mode == 'Botones':
    st.subheader("Modo: Botones")

    # Crear histograma
    hist_button = st.button('Construir histograma')
    if hist_button:
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')
        fig_h = px.histogram(car_data, x="odometer")
        st.plotly_chart(fig_h, use_container_width=True)

    # Crear gráfico de dispersión
    disp_button = st.button('Construir gráfico de dispersión')
    if disp_button:
        st.write(
            'Creación de un gráfico de dispersión para relación precio y millas recorridas')
        fig_s = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig_s, use_container_width=True)

# Crear gráficos con casillas
elif mode == 'Casillas':
    st.subheader("Modo: Casillas de verificación")
    hist_checkbox = st.checkbox('Construir histograma')
    if hist_checkbox:
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')
        fig_h = px.histogram(car_data, x="odometer")
        st.plotly_chart(fig_h, use_container_width=True)

    disp_checkbox = st.checkbox('Construir gráfico de dispersión')
    if disp_checkbox:
        st.write(
            'Creación de un gráfico de dispersión para relación precio y millas recorridas')
        fig_s = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig_s, use_container_width=True)
