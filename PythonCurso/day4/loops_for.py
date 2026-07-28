# For se repite por una cantidad definida de veces

nombres = ["Sebastoan", "Ana", "Adri", "Andres"]

for nombre in nombres: 
    if nombre.startswith("A"):
        print(f'Hola, {nombre}')

lista_listas = [[1,2],[5,7],[8,4]]

for a,b in lista_listas:
    print(a,b)

diccionario = {
    "Nombre":"Sebastian",
    "Edad" : 24,
    "Ocupación" : "tester"
    }

for clave, valor in diccionario.items():
    print(f'La clave "{clave}" tiene el valor "{valor}"')
    