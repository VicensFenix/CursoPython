# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el CSV, asumiendo que la primera fila contiene cabezales
df = pd.read_csv("Archivos_problemas_graficos\\dispersion.csv",names=["Tiempo", "Dinero"], header=None)

# Crear el gráfico de dispersión
sns.scatterplot(data=df, x='Tiempo', y='Dinero')

# Mostrar el gráfico
plt.show()