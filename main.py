from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values

from auth import router as auth_router
from question_input_route import router as input_router


config = dotenv_values(".env")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the SPECIAL ROUTER DESIGN Test from NicK!"}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(auth_router)
app.include_router(input_router)
