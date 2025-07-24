futbolistas = {
    "nombre" : "Lionel Messi",
    "Equipo" : "Barcelona",
    "Edad" : 34,
    "Altura" : 1.69
}

# Devuelve las claves
claves = futbolistas.keys()


# Devuelve el valor de una clave
getvalor_futbolista = futbolistas.get("Nombre")


# Elimina un elemento
futbolistas.pop("Edad")
print(futbolistas)


# Para iterar el dicts
futbolistas_iterable = futbolistas.items()
print(futbolistas_iterable)

# Limpiar el diccionario
futbolistas.clear()
print(futbolistas)