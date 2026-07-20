'''
Colección de datos que tienen un comportamiento especial
Es porque solo admiten elementos únicos, por lo que los duplicados los descarta, no estan ordenados en indices,
son inmutables
Solo se pueden poner tuplas como estructura anidadas 
'''

mi_set = set([1,2,3,4,5])

mi_set2 = {2,3,45,6,6}

print(mi_set)
print(mi_set2)
# print(mi_set[0]) NO se puede hacer
# mi_set2[3] = 5 No se puede hacer 
print( 3 in mi_set2)

mi_set2.add(4)
print(mi_set2)
mi_set2.remove(45)
print(mi_set2)
elemento_aleatorio =mi_set.pop() #Quita el elemento al azar
print(mi_set)

