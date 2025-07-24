# Si el modulo estuviera dentro de una carpeta en la misma ruta
# import funciones_buenas.saludar as m_saludar

# Importamos que proporciona acceso a algunas variables y funciones relacionadas con el intérprete de Python y el entorno de ejecución.
import sys

# En una lista que contiene las rutas de directorios se agrega una nueva ruta
sys.path.append("D:\\CursoPython\\funciones_buenas")
# Checamos las rutas de los modulos
# print(sys.path)

# Ahora si podemos importar el modulo y le asignamos un nombre
# Aunque salga como un error se debe ignorar porque aun asi sirve
import saludar as modulo_saludo

print(modulo_saludo.saludar("Dalto"))