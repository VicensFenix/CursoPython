# Importamos modulos
import csv

# Abrimos el archivo desde la ruta especifica con with open con una codificaión universal (UTF-8) a "archivos"
with open("Archivos\\datos.csv",encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)