"""
MODULOS
Codigo externo a nuestro fichero que lo podemos utilizar en nuestro fichero
"""
# para importar un modulo se hace con la palabra iport y el nombre del fichero
import modulo
from funciones import (
    sumaDosValores,
)  # importar una sola funcion dese un modulo en especifico


modulo.sum(
    5, 12, 11
)  # Para mostrar la funcion en consola se usa el nombre del modulo.funcion

sumaDosValores(5, 2)
import math  # Mtah es un modulo que trae python que nos permite hacer operaciones matematicas

print(math.pi)