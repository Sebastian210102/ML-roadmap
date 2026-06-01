from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt  # Usamos PyJWT moderno
import bcrypt  # Usamos bcrypt nativo
from datetime import datetime, timedelta, UTC

SECRET_KEY = "0b2faf5e31953305171049e30175e597b91d1b3158e24c598d8872a9b61fb861"
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1 # un minuto de duarcion de autenticación 



router = APIRouter(tags=["Auth-jwt"])

outh2 = OAuth2PasswordBearer(tokenUrl="login")


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
    return None

def serch_user(user_name:str):
    if user_name in users_db:
        return User(**users_db[user_name])

async def auth_user(token: str = Depends(outh2)):

    exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail="Credenciales de autentización invalidas", 
                                headers={"WWW-Authenticate":"Bearer"})
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM).get("sub")
        if username is None: 
            raise exeption
         
    except jwt.InvalidTokenError:
        raise exeption    
    
    return serch_user(username)


#Criterio de dependencia
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Usuario inactivo", 
                            headers={"WWW-Authenticate":"Bearer"})
    return user 
    

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no existe") 
    
    user = serch_user_db(form.username)

    #Convertir los datos a bytes para validar
    password_bytes = form.password.encode('utf-8')
    hash_bytes = user.password.encode('utf-8')
    #comparar el texto plano con hash, si no coenciden se lanza el error
    if not bcrypt.checkpw(password_bytes, hash_bytes): #comparar contraseñas para ver si son iguales
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña no es correcta") 


    

    acces_token = {"sub":user.username, 
                   "exp":datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_DURATION) }

    #Criframos el token 
    token_cifrado = {
        jwt.encode(acces_token, SECRET_KEY, algorithm=ALGORITHM)
    }
    return{"acces_token": token_cifrado,"token_type": "bearer"} # Esto es lo que tenemos que manejar cuando estemos llamando a nuestra API


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user