from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000/
@app.get("/")
async def root():
    return "Hola FastAPI!"

#http://127.0.0.1:8000/url
@app.get("/url")
async def url():
    return { "url_curso":"https://moredev.com/python" }

