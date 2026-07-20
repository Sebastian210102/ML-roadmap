'''
Son inmutables, no se pueden cambiar una vez que se definieron, se utilizan normalmente porque 
Ocupan menos espacios de memoria, se utilizan cuando no quieres que algo se modifique 
'''

mi_tuple = (1,2,(10,20))
mi_lista = list(mi_tuple)


print(mi_tuple[2][0])
# mi_tuple[0] = 3 Esto no es posible
print(type(mi_lista))

mi_lista[0] = 3

mi_tuple = tuple(mi_lista)
print(mi_tuple)

t = (1,2,3) 

a,b,c = t #Desempacar 
print(a,b,c)

print(t.count(2))
print(t.index(3))
