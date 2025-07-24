# Falto el profe y los alumnos van armar la clase

# Pedir el nombre y la edad de los compañeros que vinierón a clase
def obtener_compañeros(cantidad_de_compañeros):
    
    # Creando la lista con los compañeros
    compañeros = []
    
    # Ejecutando un for para pedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        # Agregando la información a la lista
        compañeros.append(compañero)
    
    # Ordanarlos de menor a mayor según su edad
    compañeros.sort(key=lambda x:x[1])
    
    # Compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir el asistente y sl profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    # Retornamos una tupla
    return asistente,profesor

# Desempaquetamos lo que nos retorna la función
asistente, profesor = obtener_compañeros(5)

# Mostramos en pantalla el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")
