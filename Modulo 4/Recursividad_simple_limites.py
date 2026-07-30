# Es una técnica donde una función se llama a sí misma para resolver un problema dividiéndolo en subproblemas más pequeños.
# Sumar todos los elementos de una lista usando recursión:

# Caso base: lista vacía suma 0
# Caso recursivo: suma(lista) = primer elemento + suma(resto de la lista)

numeros = [1, 4, 5, 9, 2, 7, 8]
def suma_lista(lista):
    if len(lista) == 0:  #caso base
        return 0  
    else:
        return lista[0] + suma_lista(lista[1:])  #caso recursivo
suma_total = suma_lista(numeros)
print(f"la suma total es: {suma_total}")
