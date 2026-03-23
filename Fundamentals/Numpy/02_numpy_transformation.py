import numpy as np 


#Target Vector
target = np.array([4,5])
#Matriz de Cizallamiento, 
shear = np.array([[1,1],[0,1]])

#Sheared Vector

sheared_vector = np.dot(shear,target)

print(f'Sheared: {sheared_vector}') 

#New vector
target = np.array([4,0])
sheared_vector = np.dot(shear, target)

print(f'shared : {sheared_vector}')

#Rotación 90°

rotation = np.array([[0,-1],[1,0]])

print(f'Matriz original {target}')
print(f'Matriz con rotación 90°: {np.dot(rotation, target)}')