from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles


app = FastAPI(  )

#Routers
#Router de productos
app.include_router(products.router)

#Router user
app.include_router(users.router)

#Staticos
app.mount("/static", StaticFiles(directory="static"), name="static") #Podemos accder a la imagen que tenemos y exponerlo

@app.get("/") #Raiz de la IP de nuestra api

async def root():
    return 'Hola FastApi'

@app.get("/url")

async def url_git():
    return { "url_github" : "https://github.com/Sebastian210102" }

