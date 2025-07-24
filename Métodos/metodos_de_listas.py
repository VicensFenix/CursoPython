# Crea una lista con list (Es una función)
lista = list([20, 12, 34, 1.80, 16,1.85]) 

# Cuenta la cantidad de elementos de una lista (Es una función) Devuelve la cantidad de elementos de la lista
resultado = len(lista)


# Agrega un elemento a la lista
lista.append(1.82)


# Agrega un elemento a lista en el indice especificado
lista.insert(2, 18)


# Agrega varios elementos a la lista
lista.extend([ 3.13, 3.10])


# Elimina un elemento de una lista, pide indice y devuelve valor
lista.pop(-3)


# Remueve un elemento de una lista, pide valor
lista.remove(12)


# Ordena una lista de forma ascendente a descendente
lista.sort()


# Invierte los elementos de una lista
lista.reverse()


# Elimina todos los elementos de una lista
lista.clear()
print(lista)
