from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Entidad usuario
class User(BaseModel):
    name: str
    surname: str
    email: str
    age: int


users_list = [
    User(name="gabriel", surname="Castro", email="gbrlcstr@hotmail.com", age=36),
    User(name="Carlos", surname="Jimenez", email="Carlos@gamil.com", age=65),
    User(name="Ana", surname="Ramirez", email="ana@gmail.com", age=68),
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


@app.get("/users")
async def users():
    return users_list
