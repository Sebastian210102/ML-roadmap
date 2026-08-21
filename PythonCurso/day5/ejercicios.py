"""
Ejercicio 1
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio
"""

def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]
    suma = sum(lista)

    if suma > 15:
        return max(lista)
    elif suma < 10: 
        return min(lista)
    else:
        lista.remove(max(lista))
        lista.remove(min(lista))
        return lista[0]


print(devolver_distintos(1,2,4))
print(devolver_distintos(10,15,30))
print(devolver_distintos(0,10,5))


"""
Ejercicio2

Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']

"""

def filtro_palabras(palabra : str):

    palabra = palabra.lower()
    lista = list(set(list(palabra)))
    lista.sort()
    return lista

print(filtro_palabras("Sebastian"))

"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def duplicidad_ceros(*args):

    for index, value in enumerate(args):
        if index == 0:
            continue
        if (args[index-1] == args[index]) and value == 0:
            return True
    return False

print(duplicidad_ceros(13,4,56,0,0))

print(duplicidad_ceros(1,2,0,1,5,6,0))


"""
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
"""


def contar_primos(tope):
    num_primos = 0
    for numero in range(2,tope+1):
        conteo = 0 
        for division in range(1,tope+1):
            if conteo > 2:
                break

            if numero%division == 0: 
                conteo += 1
        if conteo <= 2:  
            num_primos += 1

    print(f'Se encontraron un total de {num_primos} numeros primos')

contar_primos(100)