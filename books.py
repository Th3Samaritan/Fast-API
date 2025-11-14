# Bismillah
from fastapi import FastAPI

app = FastAPI() # this allows uvicorn to know that we are creating a fastapi server
@app.get("/")
async def first_api():
    return {"message": "Hello World"}