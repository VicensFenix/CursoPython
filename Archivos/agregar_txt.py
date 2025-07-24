with open("Archivos\\prueba.txt","a",encoding="UTF-8") as archivo:
    
    # Agregar un espacio en linea al principio
    archivo.write("\n")
    # Usando un bucle para agregar varias lienas
    for i in range(5):
        # Agregando lineas
        archivo.write(f"Linea {i+1} agregada\n")