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