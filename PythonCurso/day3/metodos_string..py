texto = "Buenas tardes, estoy feliz, tengo algo bueno que contarte"

F = "is for friends who do stuff together"
U  = "is for you and me, try it"
N = "is for anywhere and anytime at all"
e = " "


print(texto.upper())
print(texto[:3].lower())
print(texto.replace("tardes", "noches"))
print(texto.split()) #Separación de vacíos 
print(texto.split(",")) # Buscamos el separador 
print(e.join([F,U,N]))
print(texto.find("x")) #Ayuda a manejar mejor erroes que index
