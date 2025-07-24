with open("Archivos\\prueba.txt","w",encoding="UTF-8") as archivo:
    
    # Sobreescrbiendo el archivo
    # archivo.write("Escribiendo desde vscode")
    
    # Agregando dos lienas con writelines
    archivo.writelines(["Que onda Master\n","¿Qué día es hoy?\n"])
    
    # Agregando otras dos lienas
    archivo.writelines(["Que onda Noob\n","¿Qué paso ayer?\n"])