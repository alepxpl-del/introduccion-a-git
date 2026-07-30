##############################
# Definir y llamar funciones #
##############################
# Una función en Python se define usando la palabra clave def, seguida del nombre de la función y paréntesis que pueden incluir parámetros. El cuerpo de la función está indentado y contiene las instrucciones que se ejecutarán cuando la función sea llamada.

# def saludar():
#      print("¡Hola, gordaaa!")
# saludar()

###################################
# Parametros y argumentos basicos #
###################################
# Son variables definidas en la declaración de la función

# def saludar(nombre):
#     print(f"hola {nombre}")
# saludar("gordi")

#############
# Ejercicio #
#############

def saludar(nombre):
     print(f"hola {nombre}")
saludar("gorda")
saludar("lucho")
saludar("nico")
saludar("feli")

def calcular_area_rectangulo(base, altura):
     area= base * altura 
     print(f"el area del rectangulo es: {area}")
calcular_area_rectangulo(12, 12)
     