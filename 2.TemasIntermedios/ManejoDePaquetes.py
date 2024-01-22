#MANEJO DE PAQUETES

#exiten dependencias de python que podemos usar en nuestra app instalandolos, para ello usamos PIP y lo hacemos desde la consola

#pip install numpay 

import numpy #sirve para hacer operaciones mas comlplejas en cuanto a numeros

print (numpy.version.version)

numpy_array = numpy.array([3,5,6,8,9,4,5,6])
print(type(numpy_array))
print(numpy_array * 2)


#pip install pandas
import pandas

# pip list --- sirve para ver el listado de las dependencias intaladas
# para desinstanlar una dependencia  --- pip uninstall pandas
#pip show numpy muestra la documentacion en la consola acerca de la dependencia

#pip install requests
#se lanza una peticion para traer los 151 pokemosn de pokeapi
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

#importar paquete made in casa ---- operaciones aritmeticas
from paquete import operacionesAritmeticas

print(operacionesAritmeticas.sum(1,4))