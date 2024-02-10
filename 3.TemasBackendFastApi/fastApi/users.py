from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Entidad usuario
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int


users_list = [
    User(id=1, name="gabriel", surname="Castro", email="gbrlcstr@hotmail.com", age=36),
    User(id=2, name="Carlos", surname="Jimenez", email="Carlos@gamil.com", age=65),
    User(id=3, name="Ana", surname="Ramirez", email="ana@gmail.com", age=68),
]


# http://127.0.0.1:8000/usersjson
@app.get("/usersjson")
async def usersjson():
    return [
        {
            "name": "Gabriel",
            "surname": "Castro",
            "email": "gbrlcstr@hotmail.com",
            "age": 36,
        },
        {
            "name": "Carlos",
            "surname": "Jimenez",
            "email": "carlos@hotmail.com",
            "age": 45,
        },
        {
            "name": "Ana Maria",
            "surname": "Ramirez",
            "email": "ana@hotmail.com",
            "age": 25,
        },
    ]

# Operaciones GET
@app.get("/users")
async def users():
    return users_list


# path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# query
@app.get("/user/")
async def user(id: int):
    return search_user(id)


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


# Operaciones POST, PUT, DELETE
