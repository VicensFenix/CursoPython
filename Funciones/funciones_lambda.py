numeros = [1,2,3,4,5,6,7,8,9]

# Creando una función lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

# Creando función comun que diga si es par o no 
# def es_par(num):
    # if(num%2==0):
        # return True

# Usando filter con una función comun
# numeros_pares = filter(es_par,numeros)

#Creando lo mismo pero con función lambda
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)

print(list(numeros_pares))