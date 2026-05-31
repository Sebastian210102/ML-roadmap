def evaluar_respuestas(code: int) -> str :
    
    if code >= 200 and code < 300:
        return "Prueba pasada exito"
    elif code >= 300 and code < 400:
        return "Redireccionando"
    elif code >= 400 and code < 500:
        return "Prueba fallida : Error del cliente"
    elif code >= 500 and code < 600:
        return "Error de servidor"
    else:
        return "Codigo no valido"

evaluar_respuestas(204)
evaluar_respuestas(301)
evaluar_respuestas(499)
evaluar_respuestas(515)
evaluar_respuestas(1)

respuesta_api = {
    "id": 1025,
    "nombre": "Sebastián Rabadán",
    "puesto": "QA Trainee",
    "habilidades": ["Python", "FastAPI", "SQL"],
    "activo": True
}

def verificar_perfil(respuesta_api: dict) -> tuple:
    nombre = respuesta_api["nombre"]
    puesto = respuesta_api["puesto"]
    habilidades_list = respuesta_api["habilidades"]
    exist_python = False
    usuario_rol = f"El usuario {nombre} tiene e puesto de {puesto}"

    for habilidad in habilidades_list:
        if habilidad.lower() == "python":
            exist_python = True
            break

    return usuario_rol, exist_python  
    
print(verificar_perfil(respuesta_api))


lista_usuarios = [
    {"id": 1, "nombre": "Ana", "status": "activo"},
    {"id": 2, "nombre": "Pedro", "status": "inactivo"},
    {"id": 3, "nombre": "Luis", "status": "activo"},
    {"id": 4, "nombre": "María", "status": "inactivo"}
]


def filtrar_activos(lista_usuarios: list) -> list:
    nueva_lista = []
    for usario in lista_usuarios: 
        if usario["status"] == "activo":
            nueva_lista.append(usario)

    return nueva_lista

print(filtrar_activos(lista_usuarios))


# def test_creacion_usuario():
#     status_esperado = 201
#     status_recibido = 200 # Simulando lo que regresó la API
    
#     assert status_recibido == status_esperado

# print(test_creacion_usuario())


def contar_frecuencia(texto:str) -> dict:
    
    diccionario_frecuencia = {}
    lista_palabreas = texto.split()

    for palabra in lista_palabreas:
        diccionario_frecuencia[palabra] = diccionario_frecuencia.get(palabra, 0) +1

    return diccionario_frecuencia

print(contar_frecuencia("Python es genial y Python es rapido")) 


def limpiar_duplicados(lista_con_duplicados: list) -> list:
    
    lista_con_duplicados = set(lista_con_duplicados)
    lista_con_duplicados = list(lista_con_duplicados)
    lista_con_duplicados = sorted(lista_con_duplicados)
    return lista_con_duplicados


print(limpiar_duplicados([4, 5, 4, 1, 2, 5, 8, 2]))


def fizzBuzz(limite: int):
    
    for i in range(limite):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i) 

fizzBuzz(30)


def obtener_aprobados(calificaciones:list) -> list:
    aprobados = [x for x in calificaciones if x >= 60]
    return aprobados
calificaciones = [85, 42, 90, 55, 60, 78, 30]
print(obtener_aprobados(calificaciones))