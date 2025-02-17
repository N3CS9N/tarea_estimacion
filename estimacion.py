import streamlit as st
import numpy as np
import scipy.stats as stats

# Título de la aplicación
st.title("Estimación Puntual y por Intervalo")

# Instrucciones para el usuario
st.write("""
Esta aplicación realiza una estimación puntual y una estimación por intervalo de confianza para la media de un conjunto de datos.
Por favor, ingresa los datos solicitados a continuación.
""")

# Solicitar datos al usuario
st.sidebar.header("Ingresa los datos")
data_input = st.sidebar.text_area("Ingresa los datos separados por comas (ejemplo: 10, 15, 20, 25):")

# Convertir los datos ingresados en una lista de números
try:
    data = np.array([float(x) for x in data_input.split(",")])
except:
    st.error("Por favor, ingresa datos válidos separados por comas.")
    st.stop()

# Mostrar los datos ingresados
st.subheader("Datos ingresados")
st.write(data)

# Calcular la estimación puntual (media muestral)
mean = np.mean(data)
st.subheader("Estimación Puntual")
st.write(f"La media muestral (estimación puntual) es: **{mean:.2f}**")

# Solicitar el nivel de confianza para el intervalo
confidence_level = st.sidebar.slider("Selecciona el nivel de confianza (%):", 90, 99, 95) / 100

# Calcular el intervalo de confianza
n = len(data)
std_error = np.std(data, ddof=1) / np.sqrt(n)
margin_of_error = stats.t.ppf((1 + confidence_level) / 2, n - 1) * std_error
confidence_interval = (mean - margin_of_error, mean + margin_of_error)

# Mostrar el intervalo de confianza
st.subheader("Estimación por Intervalo")
st.write(f"El intervalo de confianza al {confidence_level*100:.0f}% es: **({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})**")

# Ejemplo previo enfocado en informática
st.sidebar.header("Ejemplo previo")
st.sidebar.write("""
Ejemplo: Supongamos que tienes los tiempos de respuesta (en ms) de un servidor web:
- Datos: 100, 105, 98, 102, 99, 104, 101, 97, 103, 100
- Nivel de confianza: 95%
""")