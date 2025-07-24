# Creando un conjunto con set
conjunto = set(["dato1"])

# Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

# Teoría de conjuntos

conjunto1 = {1,3,-10,7}
conjunto2 = {1,3,7}

# Verificamos si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# Verificamos si es un super subconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

# Verificar si hay algún  número en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)