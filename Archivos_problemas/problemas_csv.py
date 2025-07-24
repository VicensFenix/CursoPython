# Importar librerías necesarias
import pandas as pd

# Leer el archivo CSV y definir los nombres de las columnas, sin usar la primera fila como encabezado
df = pd.read_csv('Archivos_problemas/datos.csv', names=["name", "lastname", "age"], header=None)

# Eliminamos filas con NaN en la columna "age"
df = df.dropna(subset=["age"])

# Convertir la columna "age" a tipo entero
df["age"] = df["age"].astype(int)

# Mostrar el tipo de dato del primer elemento de la columna "age"
print(type(df["age"][0]))

# Reemplazar los valores "dalto" por "maestro" en la columna "lastname"
df['lastname'].replace("dalto", "maestro", inplace=True)

# Mostrar la columna "lastname" después del reemplazo
print(df["lastname"])

# Eliminar filas que contienen valores NaN en otras columnas, si es necesario
df = df.dropna()

# Eliminar filas duplicadas basadas en todas las columnas
df = df.drop_duplicates()

# Creando el CSV con el DataFrame resultante (limpio)
df.to_csv('Archivos_problemas/datos_limpios.csv', index=False)

# Mostrar el DataFrame final
print(df)