import numpy as np

'''
l Reto Técnico:
Demuestra que los vectores canónicos 
$\hat{i} = [1, 0]$ y $\hat{j} = [0, 1]$ son una base para llegar a cualquier punto en 2D.

'''
#Definir los vectores canónicos
i_hat = np.array([1, 0])
j_hat = np.array([0, 1])


#Definimos que queremos llegar a un punto (42, 24)
#Recordamos que si un vector es Linealmente independiente, entonces podemos escribir
#  cualquier vector como una combinación lineal de los vectores canónicos.

target = np.array([42, 24])

resultado = 42 * i_hat + 24 * j_hat

#podemos ver que se cumple la ley ya que el resultado es igual al target.
#Demostramos que el SPAN de los vectores canónicos es igual a todo el espacio 2D, lo que 
# significa que cualquier punto en 2D se puede alcanzar mediante una combinación lineal 
# de estos vectores.
print("Resultado:", resultado)

matrix = np.array([i_hat, j_hat])
#Verificamos que los vectores canónicos son linealmente independientes
determinant = np.linalg.det(matrix)
print("Determinante de la matriz formada por los vectores canónicos:", determinant)
#si el determinante es diferente de cero, entonces los vectores son
#  linealmente independientes.


# 1. Crea un array de 10 números aleatorios entre 0 y 100

array = np.random.randint(0,101, size = 10)
print(array)
# 2. Imprime el promedio, máximo y mínimo
print(f'El máximo es {np.max(array)}')
print(f'El mínimo es {np.min(array)}')
print(f'El promedio es {np.mean(array)}')

# 3. Normalízalo (valores entre 0 y 1)

normalization = (array-np.min(array)) / (np.max(array) -np.min(array))
print(f'''
Normalizando el arreglo: 
      {normalization}
''')
# 4. Imprime cuántos valores están por encima del promedio original

count = 0
promedio = np.mean(array)
for dato in array:
    if dato > promedio:
        count+=1
print(f"Hay {count} datos por encima del primedio")
count = 0
count = np.sum(array > promedio)
print(count)