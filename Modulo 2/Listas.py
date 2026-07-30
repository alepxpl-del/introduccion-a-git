# LISTAS #
##########
# Permiten: int(nº entero), float (nº decimal), str (string/cadena de txt), booleano (True/False)
pjs_DBZ = ["Goku", "Vegeta", "Trunks", "Gohan", "Bardock", "Luffy", "Piccolo", "Krilin"]

# Mutabilidad #
###############
pjs_DBZ[5] = "Bulma" # Modifica un elemento de la lista segun el orden de indice
pjs_DBZ.append("Freezer") # Agrega un elemento a la lista

# Indexado #
############
#print(pjs_DBZ[4])# de 0 a inf va en orden normal desde el principio
#print(pjs_DBZ[-4])# de -1 a -inf va en orden contrario desde el final

# Slicing #
###########
#seleccion = pjs_DBZ[1:6] # Crea una sublista a partir del indice de los elementos de la misma
#print(seleccion)

# Metodos comunes #
###################
#pjs_DBZ.append("Broly") # Agrega un elemento al final de la lista
#pjs_DBZ.pop() # Devuelve y elimina el ultimo elemento de la lista
#pjs_DBZ.pop(2) # Devuelve y elimina el elemento espicificado 
#pjs_DBZ.remove("Gohan") # Elimina la primera aparicion de un elemento
#pjs_DBZ.extend(["Goku Black", "Bills", "Wiss", "Caulifla", "Zenozama"]) # Extiende la lista agregando los elementos de otra
pjs_DBZ.insert(7, "Majin Boo") # Inserta un nuevo elemento en el indice especificado
print(pjs_DBZ)