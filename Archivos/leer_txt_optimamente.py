# Abriendo el archivo con whit open
with open("Archivos\\prueba.txt",encoding="UTF-8") as archivo:
    
    # Leemos el archivo
    contenido = archivo.read()
    
    # Mostramos el archivo
    print(archivo.read())
    
# No es necesario cerrarlo al usar whit open