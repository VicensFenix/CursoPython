# Creando una función simple
# def saludar():
    #print("Hola Mundo, saludos desde Python")
    
# Ejecutar la función simple
#saludar()

# Crear una función que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "alumna"
    elif (sexo == "hombre"):
        adjetivo = "alumno"
    else:
        adjetivo = "alumne"
    print(f"Hola {nombre}, {adjetivo} ¿Cómo estas?")
    
saludar("Omar","Hombre")
saludar("Danna","MUJER")
saludar("Jafet","inclusive")


def crear_contrasena_random(num):
    chars = "abcdfghij"
    num_str = str(num)
    # Tomar el primer dígito como número
    num_digito = int(num_str[0])
    
    # Calcular índices asegurándose que estén en rango
    c1 = max(0, num_digito - 2)
    c2 = min(len(chars) - 1, num_digito)
    c3 = max(0, num_digito - 5)
    
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num_digito * 2}"
    return contrasena

password = crear_contrasena_random(2)
frase = f"Tu contraseña nueva es: {password}"
print(frase)
    