from fastapi import FastAPI
from auth import router as auth_router
from userDB import router as user_db_router
from pymongo import MongoClient
from dotenv import dotenv_values


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

# app.include_router(user_db_router, prefix='/users')
app.include_router(auth_router)