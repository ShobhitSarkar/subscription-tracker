from fastapi import APIRouter, FastAPI
from api import create, update, read, delete


app = FastAPI()

app.include_router(create.router)
app.include_router(update.router)
app.include_router(read.router)
app.include_router(delete.router)


@app.get("/")
async def root():
    return {"message": "Welcome home!"}

