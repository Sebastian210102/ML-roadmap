'''
1. Son inmutables
2. Pueden concatenarse
3. Multiplicable
4. multilineales

'''

#Inmutables

nombre = "Sebastian"
nombre[0] = "K" 
print(nombre) # No es posible 


#Concatenarse

saludo = "Hola"
print(saludo + nombre) #HolaSebastian

#Multiplicar

print(saludo*3) #HolaHolaHola

#Multilinear

frase = "Que onda como estamos\nAyer te busque pero no estabas\nQue tal hoy"
frase2 = '''Que onda como estamos
Ayer te busque pero no estabas
Que tal hoy'''

print(frase)
print(frase2)

print("onda" in frase) # True 
print(len(nombre)) #Longitud de el string