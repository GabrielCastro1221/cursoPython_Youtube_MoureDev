"""
DICCIONARIOS
Los diccionarios agrupan valores con clave valor.
Sirve para relacionar datos
"""

# Sintaxis
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Elementos con clave valor Es como un Array de objetos en JS.
my_other_dict = {"nommbre": "gabriel", "apellido": "castro", "edad": 35}
print(my_other_dict)

# Se pueden poner una clave con varios valores
my_dict = {
    "nombre": "gabriel",
    "apellido": "castro",
    "edad": 35,
    "lenguajes": {"python", "Swift", "Kotlin"},
}
print(my_dict)

# Nos muestra cuantos elementos clave valor tiene el diccionario
print(len(my_other_dict))
print(len(my_dict))

# NOTA: pudo tener un diccionario dentro de otro diccionario

# Para buscar un elemento basta con colacar el nombre de la clave, y asi se muestra el valor
print(my_dict["nombre"])

# Cambiar el valor de la clave
my_dict["nombre"] = "pedro"
print(my_dict["nombre"])

# Agregar una nueva clave valor al diccionario
my_dict["calle"] = "french"
print(my_dict)

"""
para eliminar una clave valor del diccionario
NOTA: No se pueden recuperar datos eliminados
"""
del my_dict["calle"]
print(my_dict)

# comprobar si una clave valor existe dentro del diccionario, Se busca por el nombre del valor no de la clave
print("nombre" in my_dict)
print("nom" in my_dict)

print(my_dict.items())  # Muestra todos los items del diccionario
print(my_dict.keys())  # Muestra las claves de los elementos
print(my_dict.values())  # Muesta los valores de los valores de lenguaje