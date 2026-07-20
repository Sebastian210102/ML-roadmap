'''
Pedir al usuario que inserte un texto,
ingrese 3 letras de su elección

devolver lo sieguiente:
1. Cuantas veces aparece cada una de las letras que eligio 
2. Cuantas palabras tiene el texto 
3. Cuál es la primera leta del texto y cual es la ultima 
4. Como sería el orden invertido de las palabras 
5. La palabra python aparece en el texto. 
'''

texto = input("Ingresa el texto que desees: ")
palara1 = input("Ingresa 1 letra de tu elección: ")
palara2 = input("Ingresa 1 letra de tu elección: ")
palara3 = input("Ingresa 1 letra de tu elección: ")
texto = texto.lower()
palabras = [palara1, palara2, palara3]

lista_palabras = texto.split()

for palabra in palabras:
    print(f"La palabra {palabra.lower()} aparece un total de {texto.count(palabra.lower())} en el texto")
lista_palabras.reverse()
texto_reves = " ".join(lista_palabras)
lista_palabras.reverse()

print(f'El texto tiene un total de {len(lista_palabras)} palabras')
print(f"La primera letra del texto es {lista_palabras[0][0]} y la ultima es {lista_palabras[-1][-1]}")
print(f'El texto al reves es {texto_reves}')
print(f'La palabra Python aparece en el texto? : {"python" in lista_palabras}')