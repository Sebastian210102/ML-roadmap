from fastapi import FastAPI

app = FastAPI()




@app.get("/") #Raiz de la IP de nuestra api

async def root():
    return 'Hola FastApi'

@app.get("/url")

async def url_git():
    return { "url_github" : "https://github.com/Sebastian210102" }

