"""
Que es una funcion: un bloque de codigo reutilizable que 
es posible usarlo y normalmente solo se ocupa de una acción 
"""

def saludo(nombre):
    print(f"Hola {nombre}")

saludo("Sebastian")

#Return va a devolver la función esto lo podemos almacenar en una varible 

def multiplicar(num1, num2):
    return num1*num2


print(multiplicar(5,10))

#Funciones dinámicas 
mi_lista = [55,99,6899, 485,567,4722]

def chequear_3_cifras(lista : list):
    lista_3_numeros = []
    for l in lista:
        if l in range(100,1000):
            lista_3_numeros.append(l)
    return lista_3_numeros

print(chequear_3_cifras(mi_lista))