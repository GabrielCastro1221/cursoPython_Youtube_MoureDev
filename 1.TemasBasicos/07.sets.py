"""
SETS
Es una estructura fija de valores
"""

# Sintaxis
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # inicialmente es un diccionario

# Una vez se llenan de datos se convierte a tipo set porque esta declarada la variable tipo set, por lo que se reconoce un tipado dinamico
my_other_set = {"gabriel", "Castro", 35, 1.77}
my_other_set_2 = {1, 2, 3, "gabriel", "Castro", 35, 1.77}
print(type(my_other_set))

# Muestra cuantos elementos contiene el set
print(len(my_other_set))

"""
Añade un elemento en el set: UN SET NO ES UNA ESTRUCTURA ORDENADA.
No se puede buscar un elemento por posicion de elemento
Cuando se intenta ingresar un mismo valor no se agrega porque esta repetido
"""
my_other_set.add("Skater")
print(my_other_set)

# Eliminar elemento del set
my_other_set.remove("Skater")
print(my_other_set)

# Comprabar si un elemento existe dentro de set
print("Ramirez" in my_other_set)
print("gabriel" in my_other_set)

# Borrar todos los elementos del set
my_other_set.clear()
print(len(my_other_set))

# Unir 2 sets
my_new_set = my_other_set_2.union(my_other_set)
print(my_new_set)

# alamcena los valores de los 2 sets sin repetir valores
print(my_other_set.difference(my_other_set_2))
