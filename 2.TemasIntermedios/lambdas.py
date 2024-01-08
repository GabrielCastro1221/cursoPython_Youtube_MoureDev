"""
LAMBDAS
SON FUNCIONES ANOMIMAS
Sintaxis 
Suma
Recibe 2 parametros y despues de los 2 puntos hae el proceso de la suma 
esta funcion se almacena en una variable para poder usarla posteriormente
"""
sum_valores = lambda valor1, valor2: valor1 + valor2
print(sum_valores(5, 12))

multiplicar_valores = lambda num1, num2: num1 * num2 - 3
print(multiplicar_valores(5, 30))


# Funcion que retorna una lambda
def sum_nums(num1):
    return lambda valor1, valor2: valor1 + valor2 + num1


print(sum_nums(4)(5, 75))
