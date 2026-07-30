# Estas estructuras permiten que tu programa tome decisiones basadas en condiciones booleanas (True o False).

# if evalúa una condición y ejecuta su bloque si es verdadera.
# elif (else if) permite evaluar condiciones adicionales si las anteriores fueron falsas.
# else captura cualquier caso que no haya cumplido las condiciones anteriores.

###########
# Ejemplo #
###########

Main = str(input("Decime cual es tu main en el lol: "))
if Main == "Irelia":
     print("sos bueno en el lol")
elif Main == "yuumy":
     print("sos una mrd de ser humano")
else:
     print("no sos bueno en el lol")

#############################################
# Control de flujo con expresiones anidadas #
#############################################

Manejo = str(input("Sabes manejar?: "))
Edad = int(input("Cuantos años tenes?: "))
if (Edad <18) and (Manejo == "si"):
    print("te van a llevar los paco")
elif (Edad >18) and (Manejo == "no"):
    print("aprende a manejar asi te sacas la licencia")
elif (Edad >18) and (Manejo == "si"):
    print("ya podes obtener tu licencia")
else:
    print("no podes hacer nada negraso suicidate")
