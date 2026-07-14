'''
Es una secuenacia ordenada de objeto, puede tener distintos tipos de datos en una sola lista
Se escriben entre corchetes

'''

mi_lista = ["a", "b", "c", 13, 34]
mi_num_lista = [1,23,4]


print(len(mi_lista))
print(mi_lista[3])

print(mi_lista + mi_num_lista)

mi_gran_lista = mi_lista + mi_num_lista

mi_gran_lista[0] = 89
print(mi_gran_lista)

mi_gran_lista.append(49)
print(mi_gran_lista)

poepado = mi_gran_lista.pop(2)

print(f'Elemento eliminado {poepado}')

nueva_lista = [1,5,8,3,6,9,2]
nueva_lista.sort()
print(nueva_lista)

nueva_lista.reverse()
print(nueva_lista)