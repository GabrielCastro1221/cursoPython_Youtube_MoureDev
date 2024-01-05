"""
VARIABLES: 
para declarar una variable en python se usa camelCase o se usa snake_case
no hay necesidad de especificar el tipo de dato python analiza la entrada del dato y asigna el tipo de dato que contiene
"""

mi_string = "string"
print(mi_string)
mi_int = 55
print(mi_int)
mi_float = 1.2
print(mi_float)
mi_bool = False
print(mi_bool)

# concatenacion de variables
print(mi_bool, mi_float, mi_int, mi_string)

# Trasnformar de int a string
mi_int_to_str = str(mi_int)
print(mi_int_to_str)

# Con estos 2 prints verificamos que el dato se haya transformado correctamente
print(type(mi_int))  # dato sin transformar
print(type(mi_int_to_str))  # dato transformado

# Funciones del sistema
mi_string = "string"
print(len(mi_string))  # cuenta cuantos caracteres tiene la variable
print("el contenido de mi variable es:", mi_string)  # print con un mensaje descriptivo

"""
#Variable en una sola linea
#NOTA: es mala practica declarar muchas variable en una sola linea
"""
nombre, apellido, alias = "Gabriel", "Castro", "Raven"
print("Mi nombre es: ", nombre, "Mi apellido es:", apellido, "Mi alias es:", alias)

# Sistema de input o prompt
nombre = input("Cual es tu nombre?")
apellido = input("Cual es tu apellido?")

print(nombre)
print(apellido)
