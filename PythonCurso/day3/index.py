'''
Un string es una cadena de caracteres por lo que tiene un ordenamiento que se puede indexar

'''

mi_texto = "Hola mundo"

print(mi_texto.index("n"))
print(mi_texto.index("o", 5))
print(mi_texto.rindex("o"))

print(mi_texto[2]) 
print(mi_texto[::])
print(mi_texto[:-1])
print(mi_texto[::-1])
print(mi_texto[4::])