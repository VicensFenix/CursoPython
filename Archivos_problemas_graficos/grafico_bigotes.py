# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el CSV, asumiendo que la primera fila contiene cabezales
df = pd.read_csv("Archivos_problemas_graficos\\bigotes.csv",names=["Categoria","valor"], header=None)

# Crear el gráfico de dispersión
sns.boxplot(data=df, x='Categoria', y='valor')

# Mostrar el gráfico
plt.show()