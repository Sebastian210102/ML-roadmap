palabra = "python"

lista = [p for p in palabra]

print(lista)

numeros = [1,23,4,5,6,8,9,34]


mayores = [numero for numero in numeros if numero > 10 ]

print(mayores)


cuadrados = [n ** 2 for n in range(0,10,2)]

print(cuadrados)

mayores = [numero if numero > 10 else "no" for numero in numeros  ]

print(mayores)