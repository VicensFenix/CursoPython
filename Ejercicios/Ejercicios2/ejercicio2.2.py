# Creando una función que nos devuelva los numeros primos
# Entre 0 y el argumento que pasamos

# Crear una función que verifique si un numero es primo
def es_primo(num):
    # Verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        # Si es divisible por alguno retornamos false y termina el ciclo
        if num%i==0: return False
    # Si termina el bucle, significa que no fue divisible entonces es primo
    return True

# Creando una función que retorne una lista con todos los primos
def primos_hasta(num):
    # Creando la lista
    primos = []
    for i in range(3,num+1):
        # Verificamos si es valor es primo
        resultado = es_primo(i)
        # En caso de que sea lo agragamos a la lista
        if resultado == True: primos.append(i)
    # Devolvemos la lista
    return primos

# Creamos el resultado llamando a la función
resultado = primos_hasta(13)
# Mostramos el resultado por pantalla
print(resultado)