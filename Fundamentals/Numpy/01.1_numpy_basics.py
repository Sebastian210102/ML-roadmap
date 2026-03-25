import numpy as np

# 1. Crea un array del 1 al 20
array = np.arange(1,21)
print(array)

# 2. Accede al elemento en la posición 5
print(array[5])
# 3. Accede a los últimos 3 elementos
print(array[-3:])
# 4. Slice del elemento 3 al 10
print(array[3:10])
# 5. Crea un array 4x4 con números del 1 al 16
array_4_4 = np.arange(1,17).reshape(4,4)
print(array_4_4)
# 6. Accede a la segunda fila completa}
print(array_4_4[1])
# 7. Accede a la tercera columna completa
print(array_4_4[:,2])
# 8. Slice del array 4x4: solo las primeras 2 filas y primeras 2 columnas
print(array_4_4[:2,:2])
# 9. Invierte el orden del array del ejercicio 1
array = array[::-1]
print(array)
# 10. Crea un array 3x3 de ceros y reemplaza la diagonal con 1s
array_ceros = np.zeros((3,3))
print(array_ceros)
np.fill_diagonal(array_ceros, 1)
print(array_ceros)
