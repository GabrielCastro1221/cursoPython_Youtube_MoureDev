"""
FUNCIONES
las funciones encapsulan logica concretra para resolver un problema
"""


# Sintaxis
# Funcion simple
def my_function():
    print("Hola python funcion")


my_function()


# Funcion con parametros
def sumaDosValores(num1, num2):
    suma = num1 + num2
    print(num1 + num2)


sumaDosValores(5, 12)


# Funcion con return
def suma_return(num1, num2):
    return num1 + num2


print(suma_return(2, 6))


#Funcion para traer textos dinamicos
def name_with_default(name, surname, alias ="sin alias"):
    print(f"{name} {surname} {alias}")
    
print("Gabriel", "Castro") #sin alias
print("Gabriel", "Castro", "Raven") #con alias
