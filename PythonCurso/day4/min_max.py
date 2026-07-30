lista = [58,96,72,64,35]

nombres = ['Juan', "Sebastian", "Alfredo"]

print(min(nombres)) #imprime el primero en orden alfabetico
print(max(nombres))
print(f'El numero mas pequeño de la lista es: {min(lista)}')
print(f'El numero mas grande de la lista es: {max(lista)}')

nombre = "sebastian"
print(min(nombre)) #Primero busca mayusculas 
nombre = "Sebastian"
print(min(nombre))