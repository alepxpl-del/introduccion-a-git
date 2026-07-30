######################
# Variables Locacles #
######################
# Se define dentro de una función y solo existe durante la ejecución de esa función. No es accesible fuera de ella.
def saludar():
    mensaje = "hola"
    print(mensaje)
saludar()
# mensaje seria la variable local de la funcion saludar, no esta definida fuera de la funcion.

######################
# Variables Globales #
######################
# Se define fuera de cualquier función y puede ser accedida desde cualquier parte del código, incluso dentro de funciones (aunque para modificarla dentro de una función se requiere la palabra clave global).
contador = 0 
def incrementar():
    global contador
    contador += 1
incrementar()
print(contador)
# contador seria la variable global, modificada dentro de una funcion

########################################
# Parámetros y argumentos en funciones #
########################################
# son variables definidas en la declaración de la función, y se les pasan argumentos al llamar la función.
def multiplicar(a, b=2): 
    return a * b
print(multiplicar(5))      
print(multiplicar(5, 3))   
# En el primer print, "b" toma el valor por defecto y se declara el valor de "a", en el segundo print, se declara el valor de "a" y se modifica el de "b"
# Esto permite reutilizar funciones con diferentes datos sin modificar su código.

###############################
# Funciones integradas útiles #
###############################
# len() para obtener la longitud de una lista o cadena
# range() para generar secuencias de números

nombres = ["Ana", "Luis", "Marta"]
print(len(nombres))  # Imprime: 3
for i in range(3):
    print(nombres[i])
