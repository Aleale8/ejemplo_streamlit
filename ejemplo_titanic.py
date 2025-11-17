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

#desplegamos un histograma con los datos del eje X
fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df["Age"], bins=div)
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")

#tomando datos para hombres y contando la cantidad
df_male = df[df["Sex"] == "hombres"]
cant_male = len(df_male)

#tomando datos para mujeres y contando la cantidad
df_female = df[df["Sex"] == "mujeres"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color = "red")
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title('Distribución de hombres y mujeres')

#desplegamos el gráfico
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
