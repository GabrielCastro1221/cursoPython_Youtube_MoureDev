"""
TUPLAS
Conjunto de valores, en las tuplas se puden usas metodos que no se pueden usar con las listas
"""
my_tupla = tuple()
my_other_tupla = (1, 2, 3, 4, 5)


# Sintaxis
my_tupla = (35, 1.77, "Gabriel", "Gabriel", "Castro")
print(my_tupla)
print(type(my_tupla))

# Imprimir por cada posicion de la tupla
print(my_tupla[0])

# Cuenta cuantas veces existe el valor dentro de la tupla
print(my_tupla.count("Gabriel"))

# Nos muestra la posicion donde se encuentra el valor en la tabla
print(my_tupla.index(1.77))

"""
No es tipado dinamico
En las tuplas no se pueden alterar los valores son CONSTANTES
saca error 

my_tupla[1] = 1.80
print(my_tupla)
"""

# Unir 2 tuplas en una tupla nueva
my_new_tupla = my_tupla + my_other_tupla
print(my_new_tupla)

# Buscar elementos entre un rango de posiciones
print(my_new_tupla[3:6])

# Cambiar una tupla a lista para alterar sus valores
Tuple = list(my_new_tupla)
print(type(Tuple))
