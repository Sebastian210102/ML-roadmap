from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, UTC
ALGORITHM = "HS256"
ACCES_TOKEN_DURATION = 1 # un minuto de duarcion de autenticación 



app = FastAPI()

outh2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

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
            "password" : "$2a$12$fGg1htnNpWlsFUUsVgm96uwbn7Zy0.4FlYjpzxbrEAS3TMAgvh4Z2" },
        "Erik" : {
            "username" : "Erik",
            "full_name" : "Erik Diaz",
            "email" : "erik@gmail.com",
            "disabled" : True,
            "password" : "$2a$12$xww5pBRVIKOwUK/s5zUHeO5v2x15QROP06Okl.gBG4nWtGdyve032" }
    }

def serch_user_db(user_name:str):
    if user_name in users_db:
        return UserDB(**users_db[user_name])
    

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe") 
    
    user = serch_user_db(form.username)


    if crypt.verify(form.password, user.password): #comparar contraseñas para ver si son iguales
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña no es correcta") 

    
    expire = datetime.now(UTC) + timedelta(minutes=ACCES_TOKEN_DURATION) 
    


    return{"acces_token": user.username,"token_type": "bearer"}