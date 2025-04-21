import streamlit as st

st.set_page_config(
    page_title='Tasador',
    page_icon='🏠',
    layout="wide",
)

st.title('🏠Predicción de pisos')
st.write('Tasador')

tab1, tab2 = st.tabs(['Resumen', 'Contacto'])

with tab1:
    st.subheader('Resumen del proyecto')
    st.write('Este proyecto consiste en una exploración y regresión de precios de pisos en Madrid.')

with tab2:
    st.subheader('Contacto')
    st.write('Autor: yo')
    st.write('Correo: yo@gmail.com')