# LISTAS = estructura para hacer operaciones muy complejas e inteligentes parecidas a los arrays pero mejores.

my_other_list = []

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Gabriel", "Castro"]
print(type(my_other_list))

# acceder a un valor especifico de la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

# cuando se pone el signo negativo por ejemplo -3 toma la primera posicision de la lista 3 el valor es castro -3 el valor es 35 si se pone -4 da error porque se exederia las posiciones de la lista


# el count cuenta cuantas veces se repite un elemento dentro de una lista
print(my_other_list.count("Gabriel"))
print(my_list.count(30))

# Destructuracion
age, height, name, lastname = my_other_list
print(name)
print(lastname)
print(height)
print(age)

# Concatenacion de listas
print(my_list + my_other_list)

"""
#Tipado dinamico
my_list = "Hola Python"
print(my_list)
print(type(my_list))
"""

# Añadir elemento  a la lista
my_other_list.append("desarrollador web")
print(my_other_list)

# Insertar elemento en cualquier posicion
my_other_list.insert(2, "Skater")
print(my_other_list)

# Eliminar elemento de la lista
my_other_list.remove("Skater")
print(my_other_list)

# Remover elemento con ese valor especifico
my_list.remove(30)
print(my_list)

# Elimina el ultimo elemento de la lista
my_list.pop()
print(my_list)

# Eliminar elemento especifico de la lista y mostrar el valor que se elimino
My_pop_element = my_list.pop(2)
print(My_pop_element)
print(my_list)

# Eliminar sin retornar el valor del elemento
del my_list[2]
print(my_list)

# Borrar todos los elementos de la lista
my_list.clear()
print(my_list)
