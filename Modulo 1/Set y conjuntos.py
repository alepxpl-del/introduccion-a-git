#######   CONJUNTO SET   ############################################
#####################################################################
#perros =["pitbull", "bull dog", "caniche", "salchicha", "caniche", "rogelio", "pitbull", "doberman"] #LISTA
#razas = set(perros) #CONJUNTO
#print(razas) #DEVOLUCION DESORDENADA Y SIN ELEMENTOD DUPLICADOS
#print("rogelio" in razas) #CHECKEAR SI ESTA "X" ELEMENTO = True
#print("zamba" in razas) #CHECKEAR SI ESTA "X" ELEMENTO = False

#####################################################################
####### METODOS Y OPERACIONES CON SET ###############################
#####################################################################
#pj_de_lol = ["janna", "irelia", "yone", "zed"] #LISTA
#correcion = set(pj_de_lol) #CONJUNTO
#correcion.add("caitlyn") #AÑADIR ELEMENTO A LA LISTA
#correcion.discard("janna") #QUITAR ELEMENTO DE LA LISTA, SI NO ESTA, NO DA ERROR
#correcion.remove("aphelios")#QUITAR ELEMENTO DE LA LISTA, SI NO ESTA, DA ERROR
#correcion.pop() #QUITAR ELEMENENTO DE LA LISTA AL AZAR
#correcion.clear() #QUITAR TODOS LOS ELEMENTOS DE LA LISTA
#print(correcion)

######################################################################
######## UNICIDAD Y COMPARACION ENTRE LISTAS/COLECCIONES CON SET######
######################################################################
#a = {"juan", "nico", "lucho", "pocho"} #SET/CONJUNTO A
#b = {"feli", "mauro", "lucho", "juancho"} #SET/CONJUNTO B
#print(a | b) #DEVUELVE TODOS LOS ELEMENTOS DE AMBOS SETS
#print(a & b) #DEVUELVE SOLO EL ELEMENTO QUE ESTA EN AMBOS SETS
#print(b - a) #DEVUELVE SOLO LOS ELEMENTOS QUE ESTAN EN EL PRIMER SET TIPEADO PERO NO EN EL OTRO
#print(a ^ b) #DEVUELVE TODOS LOS ELEMENTOS, EXCEPTO EL QUE ESTA EN AMBOS SETS