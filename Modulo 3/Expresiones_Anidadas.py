# Una expresión anidada es una expresión que contiene dentro de sí otra expresión.

########################
# Orden de Presedencia # 
########################
# 1. () .Parentesis (mayor presedencia)
# 2. ** .Potencia
# 3. *, /, //, % .Multiplicacion y Division
# 4. +, - .Suma y Resta

###########
# Ejemplo #
###########
resultado= 2**2 * 2 / 2 + 2 - 6
print(resultado)
resultado= 2**2 * 2 / (2 + 2) - 6
print(resultado)

##################################################
# Expresiones condicionales anidadas (ternarios) #
##################################################
# Python permite usar expresiones condicionales en una sola línea, conocidas como operadores ternarios: 
x= 22
resultado= "impar" if x / 2 == 11 else "par"
print(resultado)
################################################
edad= int(input("buenas, igresa tu edad: "))
categoria= "menor" if edad <18 else("mayor" if edad <65 else "viejaso")
print(categoria)