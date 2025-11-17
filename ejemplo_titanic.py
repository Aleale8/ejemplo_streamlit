import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("database_titanic.csv")

# Muestra un título y una descripción en la aplicación Streamlit.
st.write("""
# Mi primera aplicación interactiva
## Gráficos usando la base de datos del Titanic
""")


# Usando la notación "with" para crear una barra lateral en la aplicación Streamlit.
with st.sidebar:
    # Título para la sección de opciones en la barra lateral.
    st.write("# Opciones")
    
    # Crea un control deslizante (slider) que permite al usuario seleccionar un número de bins
    # en el rango de 0 a 10, con un valor predeterminado de 2.
    div = st.slider('Número de bins:', 0, 10, 2)
    
    # Muestra el valor actual del slider en la barra lateral.
    st.write("Bins=", div)
with st.sidebar:
    # Título para la sección de opciones en la barra lateral.
    st.write("# Opciones de Visualización")
    
    # Crea un control deslizante (slider) que permite al usuario seleccionar un número de bins
    div = st.slider('Número de bins para el Histograma de Edades:', 1, 10, 5) 
    st.write("Bins seleccionados:", div)
    
    #selectbox
    st.markdown("---") # Separador visual
    selected_color = st.selectbox(
        'Elige el color base para los gráficos:',
        ('Azul Cielo', 'Rosa Fresa', 'Verde Menta', 'Púrpura Mágico', 'Rojo Clásico')
    )
    
    # Mapeo de colores para todos los selectbox
COLOR_MAP = {
    'Azul Cielo': '#66c2ff',
    'Rosa Fresa': '#ff66b2',
    'Verde Menta': '#77dd77',
    'Púrpura Mágico': '#9a67ea',
    'Rojo Clásico': '#ff4c4c',
    'Gris Neutro': '#AAAAAA'
}

# --- BARRA LATERAL (SECCIÓN DE OPCIONES Y SELECTBOX) ---
with st.sidebar:
    # Título para la sección de opciones en la barra lateral.
    st.write("# Opciones de Visualización 🦇")
    
    # Crea un control deslizante (slider) que permite al usuario seleccionar un número de bins
    div = st.slider('Número de bins para el Histograma de Edades:', 1, 10, 5) 
    st.write("Bins seleccionados:", div)
    
    st.markdown("---") # Separador visual
    
    # ----------------------------------------------------
    # SELECTBOX INDIVIDUAL 1: Color para Histograma de Edades
    # ----------------------------------------------------
    color_hist_name = st.selectbox(
        '🎨 Color para el Histograma de Edades:',
        ('Púrpura Mágico', 'Azul Cielo', 'Rosa Fresa', 'Verde Menta', 'Rojo Clásico'),
        index=0 # Púrpura Mágico como predeterminado
    )
    bar_color_hist = COLOR_MAP[color_hist_name]

    st.markdown("---") # Separador visual
    
    # ----------------------------------------------------
    # SELECTBOX INDIVIDUAL 2: Color para Distribución por Sexo
    # ----------------------------------------------------
    color_sex_name = st.selectbox(
        '🎨 Color principal para Distribución por Sexo:',
        ('Azul Cielo', 'Rosa Fresa', 'Verde Menta', 'Púrpura Mágico', 'Rojo Clásico'),
        index=0 # Azul Cielo como predeterminado
    )
    bar_color_sex = COLOR_MAP[color_sex_name]
# --- Gráficos Originales (Histograma de Edad y Distribución por Sexo) ---
st.write("### Gráficos de Distribución de Población")
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

# Histograma de Edades
ax[0].hist(df["Age"].dropna(), bins=div, color='#9a67ea', edgecolor='black')
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de Edades")

# Distribución de Hombres y Mujeres
df_sex_counts = df["Sex"].value_counts()
ax[1].bar(df_sex_counts.index, df_sex_counts.values, color=['#ff66b2', '#66c2ff'])
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title('Distribución por Sexo')

# Desplegamos el gráfico
st.pyplot(fig)

st.write("""
## Muestra de datos cargados
""")
# Graficamos una tabla
st.table(df.head())


#agrupacion por sexo
st.write("Sobrevivientes por sexo")

#grupar los datos para contar los sobrevivientes y no sobrevivientespor sexo.
survivors_by_sex = df.groupby(['Sex', 'Survived']).size().unstack(fill_value=0)

#renombrar las columnas
survivors_by_sex.columns = ['No Sobrevivió', 'Sobrevivió']

#crear un nuevo gráfico de barras
fig_survivors, ax_survivors = plt.subplots(figsize=(6, 4))
survivors_by_sex.plot(kind='bar', 
                      ax=ax_survivors, 
                      rot=0, # Mantiene las etiquetas de "Sex" horizontales
                      color={'Sobrevivió': '#77dd77', 'No Sobrevivió': '#ff6961'})

ax_survivors.set_title('Supervivencia por Sexo')
ax_survivors.set_xlabel('Sexo')
ax_survivors.set_ylabel('Número de Personas')
ax_survivors.legend(title='Estado')

#desplegamos el gráfico en Streamlit
st.pyplot(fig_survivors)

#mostrar la tabla de conteo
st.write("#Tabla de Conteo de Sobrevivientes")
st.dataframe(survivors_by_sex)


#muestra de datos cargados
st.write("""
# Muestra de datos cargados
""")
#graficamos una tabla con las primeras 5 filas
st.table(df.head())



