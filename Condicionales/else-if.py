# ingreso_mensual = 100000

# Si  la condición se cumpla
# if ingreso_mensual > 100000:
    # print("Estas bien economicamente en latam")
# En caso si la primer condición no se cumpla
# elif ingreso_mensual > 10000:
    # print("Estas bien en cualquier parte del mundo")
# En caso de que ninguna condición se cumple
# else:
    # print("Eres pobre")

cantidad_combustible = 22

# Verifica si el tanque está lleno
if cantidad_combustible == 100:
    print("El tanque de gasolina está lleno")
# Verifica si el tanque está a la mitad
elif cantidad_combustible >= 50:
    print("El tanque de gasolina está a la mitad")
# Verificia si el tanque de gasolina es bajo
elif cantidad_combustible <= 25:
    print("Tiene menos de un gasolina")
# Verifica si el nivel de gasolina es bajo y recomienda pasar a la gasolinera
elif cantidad_combustible >= 5:
    print("Pase a una gasolinera urgentemente")
# En cualquier otro caso, asumiendo que tiene algo pero no cumple las condiciones anteriores
else:
    print("No tiene gasolina")