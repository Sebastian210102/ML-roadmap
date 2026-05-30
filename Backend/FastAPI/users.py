from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#Definiendo una entidad para usuarios


class User(BaseModel):
    name: str
    surname: str
    git_url: str
    age : int

#Simulando una base de datos
users_fake_db = [User(name = "Sebastian",surname ="Rabadan",git_url = "https://github.com/Sebastian210102", age = 24),
                 User(name = "PlinPlin",surname ="Rabadan",git_url = "https://github.com/", age = 2),
                User(name = "Logan",surname ="Sargen",git_url = "https://github.com/LoganSargen", age = 35)]    

#Esto noo es lo comun y no esta bien 
@app.get("/users")
async def usersjson():
    return [{"name":"Sebastian", "surname":"Rabadan", "git_url" : "https://github.com/Sebastian210102", "age" : 24},
            {"name":"PlinPlin", "surname":"Rabadan", "git_url" : "https://github.com", "age" : 2},
            {"name":"Logan", "surname":"Sargen", "git_url" : "https://github.com/LoganSargen", "age" : 35}]

@app.get("/users")
async def users():
    return users_fake_db