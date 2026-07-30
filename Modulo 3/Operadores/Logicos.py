# Los operadores lógicos permiten combinar múltiples condiciones y evaluar expresiones booleanas más complejas.
# Devuelve valor booleano (True/False)
# Pueden contener numeros y strings
edad = 21
sos_mayor_de_edad = True

# and #
# Con un solo valor False el resultado es False
# True and True = True
# True and False = False 
# False and False = False
print(edad >=18 and sos_mayor_de_edad)

# or #
# Con un solo valor True el resultado es True
# True or True = True
# True or False = True
# False or False = False
print(edad < 18 or sos_mayor_de_edad)

# not #
# Convierte un valor True a False
# No importa el tipo de dato
# not True
print(not sos_mayor_de_edad)
