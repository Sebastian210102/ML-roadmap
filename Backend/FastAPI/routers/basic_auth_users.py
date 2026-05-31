from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # La primera gestiona la autotenticacion y la segunda la forma que se envia a nuestro backend los criterios

app = FastAPI()
#Sistema de autenticacion
oauth2 = OAuth2PasswordBearer(tokenUrl="/login")


#Esta serían los datos que se van a manejar por la red 
class User(BaseModel):
    username:str
    full_name: str
    email: str
    disabled : bool

#Usuario de base de datos
class UserDB(User):
    password : str



users_db = {
        "Sebas" : {
            "username" : "Sebas",
            "full_name" : "Sebastian Rabadan",
            "email" : "sebas@gmail.com",
            "disabled" : False,
            "password" : "123456" },
        "Erik" : {
            "username" : "Erik",
            "full_name" : "Erik Diaz",
            "email" : "erik@gmail.com",
            "disabled" : True,
            "password" : "654321" }
    }


def serch_user_db(user_name:str):
    if user_name in users_db:
        return UserDB(**users_db[user_name])
    
def serch_user(user_name:str):
    if user_name in users_db:
        return User(**users_db[user_name])
    
#Criterio de dependencia
async def current_user(token:str = Depends(oauth2)):
    user = serch_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autentización invalidas", 
                            headers={"WWW-Authenticate":"Bearer"})
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo", 
                            headers={"WWW-Authenticate":"Bearer"})
    return user 

#Es necesario poner /login porque es lo que dijimos en nuetro oauth
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe") 
    
    user = serch_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña no es correcta") 
    
    return{"acces_token": user.username,"token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
