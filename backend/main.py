from fastapi import FastAPI
import sys

sys.path.append("..")
from routes import users
from db import models, engine

app = FastAPI()

app.include_router(users.router,prefix="/api/users")

@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)

@app.get("/") 
async def root():
    return {"message": "Hello World"}