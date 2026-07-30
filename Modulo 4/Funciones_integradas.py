# Python incluye muchas funciones predefinidas que simplifican tareas comunes:

len() # Devuelve la longitud de un objeto >>>>len([1,2,3]) # 3

sum() # Suma elementos de un iterable numérico >>>>sum([10,20,30]) # 60

min(), max() # Devuelven el valor mínimo o máximo >>>>min([5,3,9]) # 3

range() # Genera una secuencia de números >>>>list(range(3)) # [0,1,2]

map() # Aplica una función a cada elemento de un iterable >>>>list(map(str, [1,2,3])) # ['1','2','3']

filter() # Filtra elementos según una función >>>>list(filter(lambda x: x>0, [-1,0,1])) # [1]
