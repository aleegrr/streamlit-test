import streamlit as st
import pandas as pd
import pickle

# Cargar el modelo (pkl)
# Recoger el input de las X -> con csv o selectores

st.title('Tasación')

opcion_entrada = st.radio(
    "¿Qué tipo de entrada quieres usar?",
    ("CSV", "Manual")
)

df_input = pd.DataFrame()

with open('models/modelo_entrenado.pkl', 'rb') as file:
    modelo, columnas = pickle.load(file)

    if opcion_entrada == 'CSV':
        archivo_cargado = st.file_uploader("Sube un archivo CSV", type=["csv"])
        if archivo_cargado:
            df_input = pd.read_csv(archivo_cargado)
    else:
        st.subheader('Introduce los datos del piso')
        input_data = {}
        for col in columnas:
            if col == 'barrio':
                input_data[col] = st.selectbox('barrio', ['Centro', 'Norte', 'Sur', 'Este', 'Oeste'])
                st.write(input_data)
            else:
                input_data[col] = st.number_input(col, value=0)
        
        df_input = pd.DataFrame([input_data])

if not df_input.empty:
    st.dataframe(df_input)

if not df_input.empty and st.button("Predecir precio"):
    df_input = pd.get_dummies(df_input)

    for col in [c for c in modelo.feature_names_in_ if c not in df_input.columns]:
        df_input[col] = 0

    df_input = df_input[modelo.feature_names_in_]
    pred = modelo.predict(df_input)[0]
    st.success(f":moneybag: Precio estimado: {int(pred):,} €")