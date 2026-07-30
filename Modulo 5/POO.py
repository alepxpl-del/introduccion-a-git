#########################
# Errores y excepciones #
#########################+

# Errores: Fallos que ocurren antes o durante la ejecución, como errores de sintaxis (SyntaxError) que impiden que el intérprete ejecute el código.

# Excepciones: Eventos que ocurren durante la ejecución y que pueden ser manejados para evitar que el programa termine abruptamente, como ZeroDivisionError o FileNotFoundError.

# Para manejar excepciones, Python ofrece la estructura try/except:
# try:
#     resultado = 10 / 0
# except ZeroDivisionError:
#     print("No se puede dividir por cero.")
# Usar try/except permite que el programa continúe funcionando incluso si ocurre un error en tiempo de ejecución.

####################
# Clases y objetos #
####################

# Clase: molde o plantilla que define las características (atributos) y comportamientos (métodos) que tendrán los objetos creados a partir de ella.

# Objeto: es una instancia concreta de una clase, con valores específicos para sus atributos.

###### Creacion de clase y objeto ######
class PjDLol:
    def __init__(self, nombre, pasiva, activa, dificultad, maestria):
        self.nombre = nombre
        self.pasiva = pasiva
        self.activa = activa
        self.dificultad = dificultad
        self.maestria = maestria
    
    def spawnear(self):
        print("una para cortar, otra para sellar")
    def saludar(self):
        print(f"Hola soy {self.nombre}")
    def habilidadpas(self):
        print(f"mi habilidad pasiva es {self.pasiva}")
    def habilidadact(self):
        print(f"mi E es {self.activa}")
    def ctrlmas6(self):
        print(f"mi dificultad es {self.dificultad}, por lo tanto es facil llegar a maestria {self.maestria}")

Main= PjDLol("Yone", "Camino del cazador", "Alma desatada", "Media", "7")
Main.ctrlmas6()