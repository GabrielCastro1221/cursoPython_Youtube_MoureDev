"""
EXCEPCIONES
Manejo de errores
"""
num1, num2 = 5, 1
num2 = "1"

"""
Con esto no tenemos manejo de errores son criterios de aceptacion
if type(num2) == int:
    print(num1 + num2)   Esto da error ya que se esta sumando un int con un str
else:
    print("No se cumple")

"""

# Manejo de errores TRY / EXCEPT
try:
    print(num1 + num2)
except:
    print("Se ha producido un error")

# Manejo de errores TRY / EXCEPT / ELSE
num3 = 5
num4 = 1
try:
    print(num3 + num4)
except:
    print("Se ha producido un error")
else:  # El else solo se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")


# Manejo de errores TRY / EXCEPT / ELSE /FINALLY
num5 = 5
num6 = 1
try:
    print(num5 + num6)
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continua correctamente")
finally:  # El finally se ejecuta siempre
    print("La ejecucion continua")


# Captura de excepciones por tipo
num7 = 5
num8 = "1"
try:
    print(num7 + num8)
except ValueError:
    # Se ejecuta solo si se produce una excepcion
    print("Se ha producido un Valueerror")
except TypeError:
    # Se ejecuta solo si se produce una excepcion
    print("Se ha producido un Typeerror")
# NOTA: los 2 except estan valiendando que clase de error esta sucediendo en este caso muestra typeError porque es erros de tipo de dato. 2 exept se usa para validar que tipo de error esta surgiendo


# Capturar errores
try:
    print(num7 + num8)
except ValueError as error:
    # Se ejecuta solo si se produce una excepcion
    print(error)
# crea una variable que almacenara el error en este caso nos muestra por consola que es un erros de tipo typeError

try:
    print(num7 + num8)
except Exception as error:  # Este except hace lo mismo que el except de arriba
    print(error)
