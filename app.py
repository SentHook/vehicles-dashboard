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
    st.write("Distribución del kilometraje de los vehículos")

    fig = go.Figure(
            data=[go.Histogram(x=car_data["odometer"])]
            )
    fig.update_layout(
            title="Distribución del kilometraje",
            xaxis_title="Kilometraje (milla)",
            yaxis_title="Cantidad de vehículos",
            )
    st.plotly_chart(fig, use_container_width=True)
