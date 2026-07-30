'''
enumerate ayuda a indexar los elementos
'''

lista = [1,2,3,4]
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

for indice, valor in enumerate(lista):
    print(indice,valor)

for indice in range(len(lista)):
    print(indice, lista[indice] )