# Creamos la lista animales
animales = ["gato","perro","loro","cocodrilo"]
numeros = [1,2,3,4,5]

# Recorre la lista animales
for animal in animales:
    print(f'El animal es un {animal}')
    
# Recorriendo la lista de numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(f'El resultado de la multiplicación es {resultado}')
    
# Iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo la lista 1: {numero}")
    print(f"Recorriendo la lista 2: {animal}")
    

# Forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])
    

# Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"Indice es: {indice} y el valor es: {valor}")
    

# Usando el for/else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")