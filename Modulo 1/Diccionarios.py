#######################################################################
############ DICCIONARIOS #############################################
#######################################################################
#Usuario1 = {"nombre": "Alejo", # DICCIONARIO DE VARIOS ELEMENTOS QUE SIEMPRE TIENEN UNA CLAVE (KEY) Y EL VALOR DENTRO DE ESA CLAVE (VALUE)
           # "contraseña": "131024",
            #"correo": "ale.px.pl@gmail.com"}
#print(Usuario1["contraseña"]) #PEDIR EL VALOR DE ALGUNA CLAVE DENTRO DEL DICCIONARIO
#Usuario1["contraseña"] = "aroncito" # CAMBIAR EL VALOR DE ALGUNA CLAVE DEL DICCIONARIO
#Usuario1["edad"] = 21 #AÑADIR NUEVA CLAVE Y VALOR AL DICCIONARIO
#del Usuario1["nombre"] #ELIMINAR UNA CLAVE CON SU VALOR DEL DICCIONARIO
#print(Usuario1.get("nombre")) #MOSTRAR VALOR DE CIERTA CLAVE Y EVITAR ERROR EN EL PROGRAMA SI LA CLAVE CON SU VALOR NO EXISTE

########################################################################
######MANIPULACION DE UN INVENTARIO CON METODOS DE DICCIONARIO##########
########################################################################
#usuarioA = {"nombre": "Giuli",  #DICCIONARIO
            #"apellido": "Guzzo",
            #"edad": "18",
            #"nacionalidad": "argentina"}
#usuarioA.clear() #ELIMINA TDO EL CONTENIDO DEL DICCIONARIO
#print(usuarioA)
#usuarios = {"user4": "Giuli", #DICCIONARIO
            #"user2": "Alejo",
            #"user5": "Enzo",
            #"user3": "Javier",
            #"user1": "Lorenzo"}
#print(usuarios)
#claves_ordenadas = sorted(usuarios) #ORDENA TODAS LAS CLAVES DEL DICCIONARIO DE MENOR A MAYOR O EN ORDEN ALFABETICO
#valores_ordenados = sorted(usuarios.values()) #ORDENA TODOS LOS VALORES DEL DICCIONARIO DE MENOR A MAYOR O EN ORDEN ALFABETICO
#claves_ordenadas_con_sus_valores = sorted(usuarios.items()) #ORDENA TODAS LAS CLAVES DEL DICCIONARIO DE MENOR A MAYOR O EN ORDEN ALFABETICO Y MUESTRA SUS VALORES
#nombre_de_usuario_x = usuarios.pop("user3") #HACE LO MISMO QUE GET PERO ELIMINA LA CLAVE
#claves_ordenadas = sorted(usuarios.keys()) #OTRA MANERA DE ORDENAR TODAS LAS CLAVES DEL DICCIONARIO DE MENOR A MAYOR O EN ORDEN ALFABETICO
#usuarios_actualizados = {"user5": "Nico", #DICCIONARIO
                         #"user6": "Juan"}
#usuarios.update(usuarios_actualizados) #ACTUALIZAR DICCIONARIO CREANDO OTRO ANTERIORMENTE
#print(usuarios)
#print(claves_ordenadas)
##### EJERCICIO #####
inventario_mc = {"madera": "23",
                 "tierra": "2",
                 "piedra": "64",
                 "espada": "1",
                 "pan": "33",
                 "diamante": "55",
                 "enderpearls": "67"}
#print(inventario_mc.get("diamant3")) 
#print(inventario_mc.get("polvora"))
#print(inventario_mc.get("polvora", "no esta ese item"))
#items_ordenados = sorted(inventario_mc.keys())
#print(items_ordenados)
#ordenar_todo = sorted(inventario_mc.items())
#print(ordenar_todo)
inventario_actualizado = {"redstone": "49",
                          "pan": "20",
                          "hierro": "11",
                          "arena": "37"}
inventario_mc.update(inventario_actualizado)
item = inventario_mc.pop("espada")
print(item)