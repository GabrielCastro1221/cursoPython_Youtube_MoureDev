# EXPRESIONES REGULARES

# lAS EXPRESIONES REGULARES NOS SIRVE PARA VALIDAR SI UNA CADENA DE TEXTO TIENE CIERTOS CARACTERES y nos retorna las ocurrencias de lo que ocurre con las expresiones regulares
import re

my_string = "Esta es la leccion número 7: Leccion Expresiones regulares"
my_other_string = "Esta no es la lleccion número6: Manejo de ficheros"

#El re.I sirve para que no tenga en cuenta ni minusculas ni mayusculas
"""
 # para usar ls expresiones regulares debemos importar este modulo
match = re.match("Esta es la leccion", my_string, re.I) # El match encuentra un patron
if match == None:
    print(match)
#match_other = re.match("Esta es la leccion", my_other_string)
#print(match_other)

#Buscar por rango
    start, end = match.span()
    print(my_string[start:end])

print(re.match("Expresiones regulares", my_string))
"""

"""
# SEARCH busca expresiones regulares en cualquier sitio de la cadena de texto

search = re.search("leccion", my_string, re.I)
print(search)
"""

"""
# FINDALL nos muestra todas las ocurrencia de la palabra leccion y las almacena en una lista
findall = re.findall("leccion", my_string, re.I)
print(findall)
"""

"""
# SPLIT busca un patron y divide la cadena de texto apartir de ahi
split = re.split(":", my_string)
print(split)
"""

"""
# SUB sustituye los valores
sub = re.sub("Expresiones regulares", "RegEx", my_string)
sub = re.sub("leccion|Leccion", "LECCION", my_string) #cambia todas lasocurrencias de ese caracter
print(sub)
"""



