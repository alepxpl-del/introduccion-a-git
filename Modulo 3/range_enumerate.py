#########
# range #
#########
# Genera una secuencia de números enteros, comúnmente usada para controlar cuántas veces se ejecuta un bucle for.
# Sintaxis básica:
# range(stop)
# range(start, stop[,step])
# start: número inicial (por defecto 0)
# stop: número donde termina (excluido)
# step: incremento (por defecto 1)

#############
# enumerate #
#############
# permite iterar sobre una colección obteniendo índice y valor simultáneamente.

spm= ["atomo", "vea", "la yunta", "jumbo"]
for puesto, super in enumerate(spm):
    print(puesto, super)