import streamlit as st

st.title('Descripción de los datos')
st.markdown('''
    - metros_cuadrados: tamaño del piso en metros cuadrados
    - habitaciones: Número de habitaciones
    - baños:Número de baños
    - garaje: si tiene garaje (1) o no (0)
    - planta: En qué planta está el piso
    - antiguedad: Años desde la construcción
    - barrio: Central, Norte, Sur, Este, Oeste
    - precio: Precio estimado del piso
    - lat: Latitud de la ubicación
    - lon: Longitud de la ubicación
    ''')