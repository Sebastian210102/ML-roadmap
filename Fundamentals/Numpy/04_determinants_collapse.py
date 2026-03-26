#Creating a DL matrix
import numpy as np

matriz_ld = np.array([[2,4],[3,6]])

print(f'Tenemos la matriz {matriz_ld}')

#Calculate determinant 

print(f'Determinante de la matroz {np.linalg.det(matriz_ld)}')

#As we can se the vectors are DL so the determinant is 0. This means that the space collapse.
try:
    inversa = np.linalg.inv(matriz_ld)
except np.linalg.LinAlgError:
    print("¡Error! La matriz es singular (determinante 0) y no se puede invertir.")

#In machine learning this its important becouse means that 2 values says the same but in
#diffetent scale, so we are counfusing the model width the same parameter but diferent scale