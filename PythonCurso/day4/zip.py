'''
Zip lo que hace es juntar dos listas en otra lista en tuplas con un elemento de cada una

'''

nombres = ['Sebastian', 'Fernanda', 'Erik']

edad = [24,30,24,55] #Zip corta los elementos 

ciudades = ["Mexico", "España", "Alemania"]
combinados = list(zip(nombres, edad, ciudades))

print(combinados)

for nombre, edad, ciudad in combinados: 
    print(f'{nombre} tiene {edad} y vive en {ciudad}')