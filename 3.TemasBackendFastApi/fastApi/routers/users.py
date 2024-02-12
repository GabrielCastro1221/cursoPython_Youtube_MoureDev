from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


# Creamos Api
# Entidad usuario
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int


users_list = []


# # Operaciones GET, POST, PUT, DELETE
@router.get("/users")
async def users():
    return users_list


# path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# query
@router.get("/user/")
async def user(id: int):
    return search_user(id)


# Post
# agregar usuario a la db
@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El esuario ya existe")
    else:
        users_list.append(user)


# Put Actualizar usuario
@router.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user


@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
