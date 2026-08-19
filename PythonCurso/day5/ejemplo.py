lista_cafes = [("Capuccino", 2.3), ( 'Frappe', 3), (("Americano", 2))]


def encotrar_cafe_caro(lista:list):

    precio_mayor = 0
    cafe_mas_caro = ""


    for cafe, precio in lista:

        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe



    return (cafe_mas_caro, precio_mayor)

print(encotrar_cafe_caro(lista_cafes))
