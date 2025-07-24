# Un array es una estructura de datos que almacena una colección de elementos
# Las arrays se cuentan desde el 0 al 9


# La lista se define con corchetes
# Una lista se puede modificar
# Una lista es una matriz de una dimensión
lista = ["Vicente",1.80,True,20]
lista[2] = False
print(lista[1])

# Una tupla se define con parentesis
# Una tupla no se puede modificar, pero si podemos reconstruir
tupla = ("Vicente",1.80,True,20)
tupla = ("Lionel",1.69,False,45,1.69)
print(tupla)

# Creando un conjunto (set)
# No tienen un orden fijo, son elementos desordenados
# No se puede modificar un elemento en especifico, pero si podemos reconstruir 
# No podemos acceder por el indice a un elemento del conjunto
# No podemos repetir valores
# Para acceder a los elementos de un set, debemos acceder desde un bucle
conjunto = {"Vicente",1.80,True,20}
conjunto = {"Hola desde Python","Hola desde Python"}
print(conjunto)

# Creando un diccionario
# Se asigna por clave : valor (key : value)
# Cada elemento se separa por comas
# Se llama al valor por la clave
# En vez de mostrar por indice(numero) muestra por dato
# No tiene un orden
diccionario = {
    'nombre' : "Cristiano",
    'apellido' : "Ronaldo",
    'pais' : "Portugal",
    'edad' : 50,
    'altura' : 1.85,
    'tiene_nivel' : True
}
print(diccionario['tiene_nivel'])
