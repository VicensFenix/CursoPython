# Importando librerías
import pandas as pd

# Usando la función read_csv para leer el archivo csv
df = pd.read_csv("Archivos\\datos.csv", names=["name","lastname","age"], header=None)
df2 = pd.read_csv("Archivos\\datos.csv", names=["name","lastname","age"], header=None)

# Obteniendo los datos de la columna nombre
nombres = df["name"]

# Ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("age")

# Ordenándolo de forma descendente
df_orden_descendente = df.sort_values("age", ascending=False)

# Concatenando los dos DataFrame
df_concatenado = pd.concat([df, df2])

# Accediendo a las primeras 3 filas con head()
primeras_filas = df.head(3)

# Accediendo a las ultimsas 3 filas con tail()
ultimas_filas = df.tail(3)

# Accediendo a la cantidad de filas y columnas con shape
filas_totales,columas_totales = df.shape

# Obteniendo datos estadisticos del DataFrame
df_info = df.describe()

# Accediendo un elemento especifico del DataFrame con loc
elemento_especifico = df.loc[2,"age"]

# Accediendo un elemento especifico del DataFrame con iloc
elemento_especifico_index = df.iloc[2,2]

# Accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

# Accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

# Accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

# Accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["age"]>30,:]

# Mostramos en pantalla el DataFrame 
print(mayor_que_30) 