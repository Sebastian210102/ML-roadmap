"""
**Kwargs = key word args


se trabaja con diccionarios

"""

def prueba(num1, num2, *args, **kwargs):

    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')


    for arg in args:
        print(f'Arg es igual a {arg}')

    for clave, valor in kwargs.items():

        print(f'Clave es {clave} tiene el valor {valor}')
        
lista_args = [1,2,4,5]

diccionarios_kwargs = {
"x" : 3, "y" : 4, "z" : 5
}

print(prueba(1,3,*lista_args,**diccionarios_kwargs))



