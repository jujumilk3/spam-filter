from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Samples

@app.get("/redirect", response_class=RedirectResponse)
async def redirect():
    return "http://localhost:8000/docs"


@app.get("/reredirect", response_class=RedirectResponse)
async def reredirect():
    return "http://localhost:8000/redirect"

