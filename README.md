# 1. Crear entorno

pipenv shell

# 2. Creado archivo app

touch app.py

# 3. Streamlit

pipenv install streamlit
streamlit run app.py

# 4. Generar archivo de requirements.txt

pipenv install pipreqs
pipreqs

# 5. Dependencias

pipenv install folium
pipenv install streamlit_folium
pipenv install plotly
pipenv install scikit-learn

NOTAS

- Para parar servidor: Ctrl+c

EXTRA

- \*args: número variable argumentos
- \*\*kwargs: número variable keyword arguments
