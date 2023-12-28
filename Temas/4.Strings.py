# STRINGS

# se puede declarar de las 2 formas con comillas simples o dobles
# sourcery skip: replace-interpolation-with-fstring, use-fstring-for-concatenation

mi_string = "mi string"
mi_string_2 = "mi string 2"

print(len(mi_string))  # cuenta cuantos caracteres tiene la string

print(
    "Mi variable 1 contiene " + mi_string + " Mi variable 2 contiene" + mi_string_2
)  # concatena muchas varibles

print(
    "Mi variable 1 contiene \n "
    + mi_string
    + "\n Mi variable 2 contiene \n"
    + mi_string_2
)  # print con salto de linea

print(
    "Mi variable 1 contiene \t "
    + mi_string
    + "\t Mi variable 2 contiene \t"
    + mi_string_2
)  # print con tabulacion

# Formateo

nombre, apellido, edad = "Gabriel", "Castro", 5

print("mi Nombre es: %s %s y mi edad es %s" % (nombre, apellido, edad))

# Desempaquetado de caracteres

lenguaje = "python"
a, b, c, d, e, f = lenguaje

# Muestra en consola cada una de las letras de la variable lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# Division

Lenguaje_slice = lenguaje[1:3]
print(Lenguaje_slice)

Lenguaje_slice1 = lenguaje[1:]
print(Lenguaje_slice1)

Lenguaje_slice2 = lenguaje[-2]
print(Lenguaje_slice2)

# Reverse

reversed = lenguaje[::-1]
print(reversed)

# Funciones

print(lenguaje.capitalize())  # primera letra mayuscula
print(lenguaje.count("t"))  # cuenta cuantas veces esta un caracter
print(lenguaje.upper())  # Mayusculas
print(lenguaje.isnumeric())  # valida si la variable es numerica
print(lenguaje.lower())  # Minuscula
