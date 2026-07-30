# Propiedades (@property) #
###########################

# Permiten controlar el acceso a atributos, simulando atributos pero con lógica detrás (getter, setter).
class Producto:
    def __init__(self, precio):
        self._precio = precio 

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

################################
# Metodos estaticos y de clase #
################################

#@staticmethod: Método que no recibe ni la instancia (self) ni la clase (cls). Funciona como función dentro de la clase, sin acceso a estado.

class Utilidades:
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

# Se usa cuando tienes una función que realiza una tarea puramente matemática o lógica de "utilidad" que no necesita leer ni modificar los datos internos de ningún objeto en particular.

#########################

#@classmethod: Método que recibe la clase como primer argumento (cls). Útil para crear métodos que afectan a la clase o para constructores alternativos.

class Usuario:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.contador += 1

    @classmethod
    def desde_cadena(cls, cadena):
        nombre = cadena.split('-')[0]
        return cls(nombre)
 
#Lleva la cuenta de cuántos usuarios se van creando.

#Permite crear usuarios a partir de un texto en lugar del formato habitual (un constructor alternativo).

###########################################
# Convenciones básicas de encapsulamiento #
###########################################

# Python no impone restricciones estrictas, pero existen convenciones:

# Prefijo _ (single underscore): indica que el atributo o método es "protegido" (uso interno, no para acceso externo).
# Prefijo __ (double underscore): activa name mangling, dificultando el acceso directo desde fuera.

class Ejemplo:
    def __init__(self):
        self._protegido = 42
        self.__privado = 99
