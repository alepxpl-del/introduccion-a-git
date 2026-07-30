# REGLAS DE 
# DESCUENTO: si compra mas de 10 unidades = -10%
#            si es cliente frecuente = -5%
precio = int(input("Ingrese el valor del producto: "))
cantidad = int(input("Ingrese la cantidad comprada: "))
cliente = input("Es cliente frecuente?: ")
cliente_frecuente = cliente == "si"
subtotal = precio * cantidad

