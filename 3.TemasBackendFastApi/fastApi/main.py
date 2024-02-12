from fastapi import FastAPI
from routers import products, users

app = FastAPI()
app.include_router(products.router)
app.include_router(users.router)


# http://127.0.0.1:8000/
@app.get("/")
async def root():
    return "Hola FastAPI!"


# http://127.0.0.1:8000/url
@app.get("/url")
async def url():
    return {"url_curso": "https://moredev.com/python"}
