import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Cargar el conjunto de datos
car_data = pd.read_csv("vehicles_us.csv")

# Contenido principal
st.header("Exploración de anuncios de vehículos usados")

st.write(
    "Aplicación interactiva para explorar anuncios "
    "de venta de vehículos."
)

st.write(f"Cantidad de anuncios: {len(car_data)}")

# Histograma interactivo
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Distribución del odometro de los vehículos")

    fig = go.Figure(
            data=[go.Histogram(x=car_data["odometer"])]
            )
    fig.update_layout(
            title="Distribución del odometro",
            xaxis_title="Kilometraje (milla)",
            yaxis_title="Cantidad de vehículos",
            )
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de Dispersión
scatter_button = st.button("Contruir gráfico de dispersión")

if scatter_button:
    st.write("Relación entre odometro y precio")

    fig = go.Figure(
            data=[go.Scatter(
                x=car_data["odometer"],
                y=car_data["price"],
                mode="markers",
                )]
            )

    fig.update_layout(
            title="Relación etnre odometro y precio",
            xaxis_title="Kilometraje (millas)",
            yaxis_title="Precio (USD)",
            )

    st.plotly_chart(fig, use_container_width=True)
