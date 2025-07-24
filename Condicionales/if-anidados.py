edad = 17
tiene_licencia = True

# Si la condición se cumple
if edad >= 18:
    # Si ambas condiciones se cumplen
    if tiene_licencia:
        print("Puedes conducir.")
    # Si la condición anidada no se cumple
    else:
        print("No puedes conducir sin licencia.")
# Si la condición no se cumple
else:
    print("Eres menor de edad, no puedes conducir.")