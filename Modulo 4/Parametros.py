# Cuando defines una función en Python con def, puedes especificar cómo recibirá los datos mediante diferentes tipos de parámetros. Estos determinan cómo se pasan los argumentos al llamar a la función.
################
# Posicionales #
################
# Son los parámetros más básicos. Se asignan en orden según la posición de los argumentos al llamar la función.

# def saludar(nombre, edad):
#     print(f"Hola {nombre}, tenes {edad} años")
# saludar("gorda", 18)

#####################
# Por palabra clave #
#####################
# Al llamar a la función, puedes especificar el nombre del parámetro, lo que permite pasar los argumentos en cualquier orden.

# def saludar(edad=25, nombre='Ana'):
#     print(f"Hola {nombre}, tenes {edad} años")
# saludar()

#######################
# Valores por defecto #
#######################
# Puedes asignar un valor por defecto a un parámetro, de modo que si no se proporciona un argumento, se use ese valor.

# def saludar(edad, nombre="Lucho"):
#     print(f"hola {nombre}, tenes {edad}")
# saludar(21)

########################
# Argumentos variables #
########################
# *args: recibe una cantidad variable de argumentos posicionales como una tupla.
# **kwargs: recibe una cantidad variable de argumentos por palabra clave como un diccionario.

def mostrar_info(*args, **kwargs):
    print('Posicionales:', args)
    print('Por palabra clave:', kwargs)
mostrar_info(1, 2, 3, nombre='Ana', edad=25)
