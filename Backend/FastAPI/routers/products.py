from fastapi import APIRouter


router = APIRouter(prefix="/products", 
                   tags=["products"], #Esto es para documentacion
                   responses={404:{"message": "No Found"}})

products_list = ["Procucto 1","Procucto 2","Procucto 3","Procucto 4","Procucto 5"]


@router.get("/")
async def products():
   return products_list


@router.get("/{id}")
async def products(id: int):
   return products_list[id]