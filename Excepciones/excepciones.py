# Función que suma dos números ingresados por el usuario
def suma_dos():
    # Iniciando un bucle para solicitar los números
    while True:
        # Solicitar al usuario que ingrese dos números
        a = input("Ingrese el primer número: ")
        b = input("Ingrese el segundo número: ")
        # Intentar convertir los números a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
            break
        # Capturar excepciones si la conversión falla
        except Exception as e:
            print("Solo se pueden ingresar números enteros.")
            print(f"Error: {e}")
        # Si todo salio bien, salir del bucle
        else:
            break
        # El finally se ejecuta siempre, independientemente de si hubo una excepción o no
        finally:
            print("Manejo de excepciones finalizado.")
    
    # Retornar el resultado de la suma
    return resultado

print(suma_dos())