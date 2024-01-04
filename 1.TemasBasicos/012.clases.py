"""
CLASES
Sirve para realizar tareas concretas. sirve para que los datos que esten dentro de esa clase tengan la misma logica
"""


# Sintaxis
class Person:
    def __init__(
        self, name, apellido, alias="Sin alias"
    ):  # El init sirve para crear un constructor de clase nota:No es una funcion.
        # el self se usa para asignar las propiedas  para su uso posterior
        self.name = name
        self.apellido = apellido
        self.alias = alias

    def Walk(self):  # Agregar metodo a una clase
        print(f"{self.name} {self.alias} Esta caminando")


my_person = Person("Gabriel", "Castro")
print(f"{my_person.name} {my_person.apellido}")  # Mostrando valores de la persona
my_person.Walk()  # Mostrando metodo caminar de clase persona


# Creando otra persona con la clase Person con parametro de alias
my_other_person = Person("Gabriel", "Castro", "Raven")
print(
    f"{my_other_person.name} {my_other_person.apellido}"
)  # Mostrando valores de la persona
my_other_person.Walk()
