#MANEJO DE FICHEROS - fileHandling
"""
# Ficheros .txt 
#para abrir al fichero usamos open y como parametro le enviamos la ruta del fichero que necesitamos 
import os
text_file = open("2.TemasIntermedios/my_file.txt", "r+") # ller y escribir
#print(text_file.read()) #lee todo el archivo DESCOMENTAR PARA VER
#print(text_file.read(10)) #con el parametro 10 solo lee los primeros 10 caracteres DESCOMENTAR PARA VER

#Leer linea a linea, cada impresion de un readLine es una linea de nuestro fichero .txt 
#print(text_file.readline()) #DESCOMENTAR PARA VER
#print(text_file.readline())#DESCOMENTAR PARA VER
#print(text_file.readlines()) #Muestra todas las lineas de nuestro fichero txt en un array de objetos DESCOMENTAR PARA VER

#iterar las lineas del fichero .txt y mostrarlas en un listado
for line in text_file.readlines():
    print(line)

#editar el fichero.txt
text_file.write("Soy skater")

for line in text_file.readlines():
    print(line)

#Borrar fichero
#os.remove("2.TemasIntermedios/my_file.txt")
"""

"""
#Ficheros Json
import json

#Crear el fichero json
json_file = open("2.TemasIntermedios/my_file.json", "r+")

json_txt = {
    "nombre": "gabriel",
    "apellido": "castro",
    "edad": 35,
    "lenguaje": "python",
    "website": "https://gabriel.com",
    "lenguajes": ["python, Js, java"]
}

json.dump(json_txt, json_file, indent=2) #nos permite pasar un objeto al archivo json.txt 
for line in json_file.readlines(): #Mostrar claves valor del fichero .json 
 print(line)

#Cargar Json -- extraer datos del json 
json_dict = json.load(open("2.TemasIntermedios/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["nombre"])
"""
