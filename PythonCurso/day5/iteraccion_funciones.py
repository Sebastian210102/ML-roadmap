from random import shuffle

#Lista inicial 
palitos= ["-","--","---","----"]


#mezaclar politos

def mezclar(lista: list):
    shuffle(lista)

    return lista

#pedir al usuario que elija

def probar_suerte():
    intento = ""

    while intento not in ["1","2","3","4"]:
        intento = input("Elige un número del 1 al 4")

    return int(intento)

#comprobar el intento del usuario


def checkear_intento(lista:list, intento):

    seleccion = intento - 1

    if lista[seleccion] == "-":
        print("Perdiste!!!")
    else:
        print("Te has salvaado")

    print(f'Te ha tocado {lista[seleccion]}')

#Flujo del programa 

palitos_mezlados = mezclar(palitos)

seleccion_usuario = probar_suerte()

checkear_intento(palitos_mezlados, seleccion_usuario)