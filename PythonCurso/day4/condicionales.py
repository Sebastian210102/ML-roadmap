'''
Da un resultaod dependeiendo de lo que va pasando a lo largo del código 

If condicion:
    accion
Elif otra_condicion:
    accopm 
else: 
    Acción
'''

variable = 'gato'


if variable == "gato" : 
    print('Tienes un gato')
elif variable == 'perro':
    print("Tienes un perro")
else: 
    print("No se que mascota tienes")

#Match permite hacer la selección

serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-10":
        print("Iphone")
    case "N-078":
        print("Motorola")
    case _:
        print("Todas las demas opciones")

#Patrones de estructuras 
# Diccionario cliente
cliente = {
    'nombre': 'Gustavo',
    'edad': 40,
    'ocupacion': 'Analista'
}

# Diccionario pelicula
pelicula = {
    'titulo': 'Matrix',
    'ficha_tecnica': {
        'protagonista': 'Keanu Reeves',
        'director': 'Lana y Lilly Wachowski'
    }
}

#Diccionario libro

libro = {"titulo":"1984",
         "autor": "George Orwell"}


elementos = [cliente, pelicula, libro]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print("Este es un cliente")
            print(nombre, edad, ocupacion)

        case {'titulo': titulo,
            'ficha_tecnica': {
                'protagonista': protagonista,
                'director': director}}:
            print("Esta es una pelicula")
            print(titulo, protagonista, director)

        case _:
            print("No se que es esto")