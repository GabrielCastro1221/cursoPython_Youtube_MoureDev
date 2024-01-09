# TIPOS DE ERRORES
# SINTAXERROR
# SintaxError = son errores de sintaxis (de escritura)
# El sistema de control dse errores de python nos muestra que es un error de sintaxis y nos da tips para arreglarlo
# print "Hola!"    #SintaxError el interprete nos dice que nos faltan parentesis. "DESCOMENTAR PARA ERROR"
print("hola")  # SintaxError Solucionado


#   NAME ERROR
# nameError = son errores dodne el interprete nos dice que la variable no esta declarada las varibales hay que escribirlas como se declararon o escribirlas bien a la hora de ejecutarlas
# print(nonmbre) #nameError = la variable nombre no esta declarada "DESCOMENTAR PARA ERROR"
# Solucion a nameError
nombre = "Gabriel"
print(nombre)


# INDEXERROR
# indexError = Este error surge cuando el inice de un elemento iterable no existe
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[4])
print(my_list[0])
print(my_list[-1])
# print(my_list[5]) #indexError "DESCOMENTAR PARA ERROR"


# MODULENOFOUNDERROR
# moduleNoFoundError = este error surge cuando no se encuentra el modulo que ha sido importado
# import maths #error "DESCOMENTAR PARA ERROR"
import math  # math bien importado

# ATRIBUTTEERROR
# atributteError = este error surge cuando ejecutamos un metodo de un modulo con errores de sintaxis
# print (math.PI)#atributteError "DESCOMENTAR PARA ERROR"
print(math.pi)  # pi con buena sintaxis


# KEYERROR
# keyError =
my_dict = {"nombre": "Gabriel", "apellido": "Castro", "edad": 35, 1: "python"}
# print(my_dict[0]) #En los diccionarios no existen las posiciones se consulta por propiedades "DESCOMENTAR PARA ERROR"
# print(my_dict["apelido"]) #HAy que escribir bien la propiedad "DESCOMENTAR PARA ERROR"
print(my_dict["apellido"])  # buena sintaxis


# TYPEERROR
# print(my_list["nombre"])# Los indices de las posiciones de las listas deben d¿ser enteros "DESCOMENTAR PARA ERROR"
print(my_list[1])  # indice de tipo entero


# ImportError
# from math import PI #para importar un proceso de un modulo ahi que escribirlo correctamen te o sale error "DESCOMENTAR PARA ERROR"
from math import pi  # Buena sintaxis


# ValueError
""" 
my_int = int("10 años") #no se deja convertir porque tiene valores numericos y de texto
print(type(my_int)) #"DESCOMENTAR PARA ERROR"
"""
my_int = int("10")
print(type(my_int))


# DivisionError
print(4 / 2)
# print(4/0) #Error porque la division no existe "DESCOMENTAR PARA ERROR"
