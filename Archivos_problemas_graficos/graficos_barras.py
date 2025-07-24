# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el CSV, asumiendo que la primera fila contiene cabezales
df = pd.read_csv("Archivos_problemas_graficos\\cofia_ingresos.csv",names=["Fuente", "Ingresos"], header=None)

# Crear el gráfico de barras
sns.barplot(data=df, x='Fuente', y='Ingresos')

# Obtener el total de ingresos
total_ingresos = df['Ingresos'].sum()

# Mostrando el total
print(f"Total de ingresos: ${total_ingresos} USD")

# Mostrar el gráfico
plt.show()