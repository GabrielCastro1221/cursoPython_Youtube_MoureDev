""" 
FUNCIONES DE ORDEN SUPERIOR 
SON FUNCIONES QUE HAEN COSAS CON FUNCIONES DENTRO
"""


# Funcion basica
def sum_one(num):
    return num + 1


def sum_five(num):
    return num + 5


# Funcion de orden superior
def sum_values_sum_one(num1, num2, f_sum):
    return f_sum(num1 + num2)


print(sum_values_sum_one(5, 6, sum_one))
print(sum_values_sum_one(5, 6, sum_five))


# Cierres
# Definir funcion dentro de otra funcion
def sum_ten(num):
    def add(value):
        return value + 10 + num

    return add


add_cierre = sum_ten(1)
print(add_cierre(5))

sum_ten(5)(1)

# Funciones de orden superior integradas en el core de python
numbers = [2, 5, 10, 21, 69]


# map: Itera cada elemento y le aplica la funcion que le hemos pasado
def multiply_two(num):
    return num * 2


print(list(map(multiply_two, numbers)))
# lo mismo que lo anterior pero con una lambda
print(list(map(lambda num: num * 2, numbers)))


# Filter
def filter_greater_than_ten(number):
    return number > 10


print(list(filter(filter_greater_than_ten, numbers)))
# lo mismo que lo anterior pero con una lambda
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
from functools import reduce


# reduce operada con un valor + el acumulador como parametros
def sum_valores(num1, num2):
    return num1 + num2


print(reduce(sum_valores, numbers))
