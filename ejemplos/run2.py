"""

"""
# Crear dos objetos de la clase 02

# objeto 01

# Creamos el objeto de la clase Asignatura
asignatura = Asignatura("Fundamentos de bases de datos", "BD-123", 4)

# crear

# Presentar objeto; usar el método __st__
print(asignatura)

# objeto 02

# crear ingresando valores por teclado del objeto de la clase AsignaturaComputacion
# input de los atributos de la clase Asignatura
nombre = input("Ingrese el nombre de la asignatura: ")
codigo = input("Ingrese el codigo de la asignatura: ")
creditos = int(input("Ingrese el numero de creditos de la asignatura: "))
lenguaje = input("Ingrese el lenguaje de programacion de la asignatura: ")
nombre_docente = input("Ingrese el nombre del docente de la asignatura: ")

mi_nueva_asignatura = AsignaturaComputacion(nombre, codigo, creditos, lenguaje, nombre_docente)
# Presentar objeto; usar el método __st__

print(mi_nueva_asignatura)


