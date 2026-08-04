'''
Proyecto del día: 

Adivinar entre el 1 y el 100 y solo tienes 8 intentos para adivinarlo. 

menor a uno o mayor a 100 - error
decir si elijio uno menor o uno mayor 
si ha acertado se le dice 
si no acepta se le va a pedir nuevamente 

'''
from random import randint

print("-----Bienvenido al juego del número secreto-------")
print("""Tendrás 8 intentos para adivinar el número entero secreto.
El número se encuentro entre el 1 y el 100 """)
top = 100
bottom = 1
numero_random = randint(bottom,top)
counter = 1
max_intentos = 8

while counter <= max_intentos:

    print(f"Este es el intento num {counter}")

    numero = int(input(f"Porfavor escribe un numero entre {bottom} y {top}: "))

    if numero == numero_random:
        print("Felicidades acertaste el número!!")
        break
    elif top < numero or numero < bottom:
        print(f"Solo se permiten números del {bottom} al {top}: ") 
        continue
    elif numero > numero_random:
        print(f"El numero es menor a {numero} ") 
    elif numero < numero_random: 
        print(f'El numero es mayor a {numero} ')
    counter += 1

    if counter > max_intentos: 
        print("Lo sentimos pero tus intentos terminaron")
        print(f"Tu número secreto es: {numero_random}")