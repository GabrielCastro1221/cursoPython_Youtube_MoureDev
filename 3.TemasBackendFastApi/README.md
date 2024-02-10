# Python para backend

## 1. instalar fastApi

### pip install fastapi["all]

## 2. importamos fastapi a la app

### from fastapi import FastAPI

## 3. llamamos fastapi en nuesta app

### app = FastAPI()

## 4. para lanzar un servidor usamos el siguiente comando dentro de la carpeta del proyecto y escribimos (el nombre del archivo:app) --reload sirve para actualizar el servidor uvicorn en tiempo real

```$ uvicorn main:app --reload```

## 5. para mirar el codigo hay que entrar al local host que asigna uvicorn

```http://127.0.0.1:8000/```

## 6. para crear rutas en nuestro documento hacemos los siguiente esta ruta nos muestra un objeto en la ruta: ```http://127.0.0.1:8000/url```

```@app.get("/url")
async def url():
return { "url_curso":"https://moredev.com/python" }
```

## 8. para acceder a la documentacion de FastAPI desde nuestro server escribimos la url: ```http://127.0.0.1:8000/docs```

## 9. para hacer consultas y peticiones usamos postman

## ¿Qué es Postman y para qué sirve?

### Las principales características y funcionalidades de Postman son: Envío de solicitudes. Permite enviar solicitudes GET, POST, PUT, DELETE y otros métodos HTTP a una API especificando los parámetros, encabezados y cuerpo de la solicitud

## 10 .Creacion de Api de usuarios

### Creamos el servidor de FastApi

``` #
from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000/users
@app.get("/users")
async def users():
    return "Hola Users!"
```

### Creamos la clase usuario

``` #
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int
```

### Creamos la Api de usuarios

``` #
# http://127.0.0.1:8000/usersjson

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
```

### Creamos la entidad usuario

``` #
class User(BaseModel):
    name: str
    surname: str
    email: str
    age: int
```

### Creamos ruta dinamica que me filtre cada usuario por su id

``` #
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
```
