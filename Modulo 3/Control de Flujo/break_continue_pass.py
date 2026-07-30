# Instrucciones para modificar el flujo dentro de bucles for y while
#########
# break #
#########
# Cuando una condición específica se cumple y no es necesario continuar iterando, break termina el bucle anticipadamente.

for numero in range(1, 10):
    if numero == 5:
        break 
    print(numero)

############
# continue #
############
# Si quieres omitir ciertas iteraciones sin terminar el bucle, continue salta a la siguiente iteración.

for numero in range(1, 10):
    if numero == 8:
        continue
    print(numero)

########
# pass #
########
# pass se usa cuando la sintaxis requiere una instrucción pero no quieres ejecutar ninguna acción aún.

for i in range(3):
    pass