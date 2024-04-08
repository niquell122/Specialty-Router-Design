from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values

from auth import router as auth_router
from question_input_route import router as input_router

config = dotenv_values(".env")
mongo_url=config["MONGO_URL"]
mongo_port=int(config["MONGO_PORT"])
db_name = config["DB_NAME"]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the SPECIAL ROUTER DESIGN Test from NicK!"}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(mongo_url, mongo_port)
    app.database = app.mongodb_client[db_name]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(auth_router)
app.include_router(input_router)
