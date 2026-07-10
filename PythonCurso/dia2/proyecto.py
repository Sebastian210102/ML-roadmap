'''
Vendedores reciben comiciones del 13%, deben meter su nombre, cuanto vendio y
se regresa su nombre y su comisión 
'''

nombre = input("Favor de ingresar tu nombre: ")
ventas = int(input("Cuales fueron tus ventas de este año?: "))

print(f"Hola, {nombre}!! \nTus comiciones con respecto a tus ventas ({ventas}) es : ${round(ventas*.13,2)}")