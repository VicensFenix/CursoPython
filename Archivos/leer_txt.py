# Usando open para abir un archivo con una codificaión universal (UTF-8) a "archivos"
archivo = open("Archivos\\prueba.txt",encoding="UTF-8")

# Leer archivo completo
# archivo = archivo.read()

# Leer linea por linea
lineas = archivo.readlines()

# Leer una sola linea
# linea = archivo.readline()

# Cerrar el archivo
archivo.close()

print(lineas)

