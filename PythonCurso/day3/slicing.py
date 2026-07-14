'''
Como poder extraer partes de un texto 

'''

texto = "Hola como estas, estoy feliz por volver a programar"

fragmento = texto[5:16]
print(fragmento)

fragmento = texto[5:]
print(fragmento)


fragmento = texto[:16]
print(fragmento)

fragmento = texto[5:16:2]

print(fragmento)

fragmento = texto[::16]
print(fragmento)

fragmento = texto[5::]
print(fragmento)
fragmento = texto[::1]
print(fragmento)