from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(tags=["Users"])

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
@router.get("/users_prueba")
async def usersjson():
    return [{"name":"Sebastian", "surname":"Rabadan", "git_url" : "https://github.com/Sebastian210102", "age" : 24},
            {"name":"PlinPlin", "surname":"Rabadan", "git_url" : "https://github.com", "age" : 2},
            {"name":"Logan", "surname":"Sargen", "git_url" : "https://github.com/LoganSargen", "age" : 35}]

@router.get("/users")
async def users():
    return users_fake_db

#Path
@router.get("/user/{id}")
async def user(id: int):
   return search_user(id)
    
#Query
@router.get("/user/")
async def user(id: int):
   return search_user(id)
    
#Agregar un usuario

@router.post("/user/", response_model=User,status_code=201)
async def user(user: User):
    
    if type(search_user(user.id)) == User :
        
        raise HTTPException(status_code=404, detail="El usuario ya existe") #Retornar errores de forma correcta
        
    users_fake_db.append(user)
    return user
#Actualizar los datos 

@router.put("/user/")
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
@router.delete("/user/")
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
    
