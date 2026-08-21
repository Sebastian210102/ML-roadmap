
"""
*args = arguments
con esto podemos definir funciones que no acepten un numero determinado de argumentos
args es una convencion pero vamos a poder utilizar esta palabra las veces que sea necesaria siempre 
y cuando se empiece con un astericos 
"""


def suma(*args):

    total = 0
    total = sum(args)
    # for arg in args:
    #     total += arg 

    return total

print(suma(2,3,4))
print(suma(2))
print(suma(2,3))
print(suma(2,3,4,34))
print(suma(2,3,4,5,6))