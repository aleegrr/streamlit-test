import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Exploración interactiva')

df = pd.read_csv('data/pisos.csv')
st.dataframe(df)

# 1. Input
st.sidebar.header('Filtros')
barrios = st.sidebar.multiselect('Barrio', df['barrio'].unique())

precio_min, precio_max = df['precio'].min(), df['precio'].max()
precio_range = st.sidebar.slider('Precios', precio_min, precio_max, (precio_min, precio_max))

hab_min, hab_max = df['habitaciones'].min(), df['habitaciones'].max()
habitaciones = st.sidebar.slider('Habitaciones', hab_min, hab_max, (hab_min, hab_max))

# 2. Filtrado
df_filtrado = df[
    df['barrio'].isin(barrios) &
    df['precio'].between(precio_range[0], precio_range[1]) &
    df['habitaciones'].between(habitaciones[0], habitaciones[1])
]

st.write('Datos filtrados:')
st.dataframe(df_filtrado)

st.subheader('Histograma de precios')
st.plotly_chart(px.histogram(df_filtrado, x='precio'))

st.subheader('Boxplot por barrio')
st.plotly_chart(px.box(df_filtrado, x='barrio', y='precio'))
