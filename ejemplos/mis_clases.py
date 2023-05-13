"""

"""

# Crear dos clases en Python

        
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Asignatura:
    nombre = ""
    codigo = ""
    creditos = 0
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

    def __str__(self):
        return "Asignatura: " + self.nombre + " Codigo: " + self.codigo + " Creditos: " + str(self.creditos)

    def obtener_nombre(self):
        return self.nombre

    def obtener_codigo(self):
        return self.codigo

    def obtener_creditos(self):
        return self.creditos

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_codigo(self, codigo):
        self.codigo = codigo

    def establecer_creditos(self, creditos):
        self.creditos = creditos

# clase 02
class AsignaturaComputacion(Asignatura):
    nombre_docente = ""

    def __init__(self, nombre, codigo, creditos, lenguaje, nombre_docente):
        super().__init__(nombre, codigo, creditos)
        self.lenguaje = lenguaje