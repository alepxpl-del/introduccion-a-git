#########
# While #
#########
# El bucle while repite un bloque de código mientras una condición sea verdadera.

contador= 0
while contador < 5:
    print (f"Contador vale {contador}")
    contador += 1

#######
# For #
#######
# El bucle for itera sobre una secuencia (como una lista, una cadena o un rango de números).

pibes= ["lucho", "nico", "feli", "juancho", "mauros"]
for pibe in pibes:
    print(pibe)

#########
# Range #
#########
# range genera una secuencia de números, comúnmente usada con for para repetir un número específico de veces.

for i in range (22):
    print(f"iteracion {i}")

#####################################
# Operadores basicos en condiciones #
#####################################
# (<, >, ==, !=, and, or, not.)

numero= 21
while numero >0 and numero != 19:
    print(numero)
    numero -= 1

########################
# Expresiones anidadas #
########################

x = 21
y = 14
z = 5
while (x > 0 and (y < 10 or z == 5)):
    print(f"{x}, {y}, {z}")
    x -= 1
    

