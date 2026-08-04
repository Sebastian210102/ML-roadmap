from random import *

aleatorio = round(uniform(1,5),2)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ["azul", "rojo", "amarillo", "verde"]

aleatorio = choice(colores)

print(aleatorio)


numeros = list(range(5, 50, 5))
print(numeros)
shuffle(numeros)

print(numeros)