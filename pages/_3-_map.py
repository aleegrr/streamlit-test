import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

data = pd.read_csv('data/pisos.csv')

# 1. Mapa
centro = [data['lat'].mean(), data['lon'].mean()]
m = folium.Map(location=centro, zoom_start=12)

# 2. Icono
icon = folium.Icon(icon='house', prefix='fa', color='blue')

# 3. Marcador
def add_marker(row):
    marker = folium.Marker(
        location=[row['lat'], row['lon']],
        popup=f'{row['barrio']} - {row['precio']}disc€',
        icon=icon
    ).add_to(m)
    marker.add_to(m)

# 4. Añadir marcadores al mapa
for index, row in data.iterrows():
    add_marker(row)

st_folium(m, width=800, height=600)