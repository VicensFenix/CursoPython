# Clase personalizada de excepción y que hereda de Exception
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"El error es: {err}")
        
# Lanzar una excepción personalizada
# raise MiExcepcion("Este es un error personalizado")

# Manejo de excepciones con la clase personalizada
try:
    raise MiExcepcion("Este es un error personalizado")
except:
    print("Se ha capturado una excepción personalizada.")
    
