# Se va a ejecutar hasta que cierta condición sea cumplida 

monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1

respuesta = "s"
while respuesta == "s":
    respuesta = input("¿Quieres seguir?(s/n)")

else:
    print("Adios")



while respuesta == "s":
    pass #Pass

nombre = input("Nombre")
for letra in nombre:
    if letra == "a":
        break #Sale
        continue # Solamente pasa a la siguiente iteración
    print(letra)