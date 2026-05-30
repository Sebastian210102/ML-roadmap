from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#Definiendo una entidad para usuarios


class User(BaseModel):
    id : int
    name: str
    surname: str
    git_url: str
    age : int

#Simulando una base de datos
users_fake_db = [User(id =1,name = "Sebastian",surname ="Rabadan",git_url = "https://github.com/Sebastian210102", age = 24),
                 User(id =2,name = "PlinPlin",surname ="Rabadan",git_url = "https://github.com/", age = 2),
                User(id = 3, name = "Logan",surname ="Sargen",git_url = "https://github.com/LoganSargen", age = 35)]    

#Esto noo es lo comun y no esta bien 
@app.get("/users_prueba")
async def usersjson():
    return [{"name":"Sebastian", "surname":"Rabadan", "git_url" : "https://github.com/Sebastian210102", "age" : 24},
            {"name":"PlinPlin", "surname":"Rabadan", "git_url" : "https://github.com", "age" : 2},
            {"name":"Logan", "surname":"Sargen", "git_url" : "https://github.com/LoganSargen", "age" : 35}]

@app.get("/users")
async def users():
    return users_fake_db

#Path
@app.get("/user/{id}")
async def user(id: int):
   return search_user(id)
    
#Query
@app.get("/user/")
async def user(id: int):
   return search_user(id)
    
#Agregar un usuario

@app.post("/user/")
async def user(user: User):
    
    if type(search_user(user.id)) == User :
        return {"error":"El usuario ya existe"}    
    else:
        users_fake_db.append(user)
        return user
#Actualizar los datos 

@app.put("/user/")
async def user(user: User): #Aqui pasamos el usuario que vamos a modificar
    found = False
    
    for index, saved_user in enumerate(users_fake_db):
        if saved_user.id == user.id:
            users_fake_db[index] = user
            found = True
            break
    if not found: 
        return {"error": "No se a actualizado el usuario"}
    return user
#Delete
@app.delete("/user/")
async def user(id :int): #Aqui solo pasamos el id ya que solo buscamos
    for index, saved_user in enumerate(users_fake_db):
        if saved_user.id == id:
            del users_fake_db[index]
            return "Usuario eliminado"
    return {"error":"No se ha eliminado el usario"}


def search_user(id): 
    users = filter(lambda user: user.id == id, users_fake_db)
    try:
        return list(users)[0]
    except: 
        return {"error":"ID no found"}
    

