# Le pedimos al usuario que nos diga una frase o varias
frase = input("Decime una frase y te calculo cuanto tardarías si tuvieras que decirla: ")

# Creamos una listas con todas las palabras de la frase (Se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

# Usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

# En caso de que tarde más de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para we tampoco me desde toda tu vida")
    
# Calculamos cuanto tardaría en decir las palabras y se lo decimos
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras / 2} segundos en decirlo')
print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos en decirlo')

