"""
CONDICIONALES
Representan la manera de establecer flujos de ejecucion en nuestro codigo, decicir que parte del codigo se va a ejecutar
"""

#Sintaxis
my_conditional = True

#si la condicion se cumple ejecuta lo que hay dentro del if
if my_conditional:
    print("Se ejecuta la condicion del if")

#si la condicion no se cumple no ejecuta lo que hay dentro del if
my_conditional = 5*3
if my_conditional == 11:
    print("se ejecuta la condicion del segundo if")

#Condicion de comparacion
if my_conditional <= 16:
    print("Es mayor que 10")
else:
    print("Es menor que 10")

#Condicion de varias comparacion
if my_conditional > 10 and my_conditional < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

#Condicion elif: condiciones con comprobaciones extra
if my_conditional > 10 and my_conditional < 20:
    print("Es mayor que 10 y menor que 20")
elif my_conditional == 1:
    print("es igual que 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

