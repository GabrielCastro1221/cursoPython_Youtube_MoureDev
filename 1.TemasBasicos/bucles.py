"""
BUCLES - LOOPS
mecanismo que sirve para iterar
"""

# Ciclo while
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:  # Este else pertenece al while
    print("mi condicion igual que 10")

# While con condicion intermedia
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecucion")
        break
    print(my_condition)


# Ciclo for
my_list = [34, 56, 78, 44, 57, 12]
for i in my_list:
    print(i)
