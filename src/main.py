from fastapi import FastAPI

app = FastAPI(docs_url='/docs')

@app.get("/")
def hi_mam():
    return "hi"


@app.get("/calc/{a}/{b}")
def hi_mam(a: int, b: int):
    return a + b


@app.post("/some-post")
def hi_mam(body: dict):
    return body['param']
