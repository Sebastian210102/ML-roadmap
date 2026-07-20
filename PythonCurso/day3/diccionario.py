'''
Es una estructura clave-valor en el cual la clave es unica, no tiene un orden común 

'''

mi_dict = {
    "nombre" : "Sebastian",
    "edad" : 24,
    "Ingeniero" : True
}

print(mi_dict)
print(mi_dict["Ingeniero"])

#Cambiar un valor y agregar una nueva clave y valor

mi_dict["edad"] = 23
print(mi_dict)

mi_dict["Leguajes"] = {"l1":"Python","l2":"JavaScript"}
print(mi_dict)

print(mi_dict["Leguajes"]["l1"])

print(mi_dict.keys())

print(mi_dict.values())
print(mi_dict.items())