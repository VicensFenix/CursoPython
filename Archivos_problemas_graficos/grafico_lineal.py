# Importamos las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos el archivo CSV
df = pd.read_csv("Archivos_problemas_graficos\\run.csv" ,names=["fecha", "distancia", "tiempo","velocidad"], header=None)

# Convertimos la columna 'fecha' a tipo datetime
sns.lineplot(data=df, x="fecha", y="distancia")

# Configuramos el formato de la fecha en el eje x
plt.plot("2023-10-07",450, marker="o")

# Mostrando el gráfico
plt.show()