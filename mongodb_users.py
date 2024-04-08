from fastapi import APIRouter
from dotenv import dotenv_values
import pymongo

router = APIRouter()

# import global variables
config = dotenv_values(".env")
db_name = config["DB_NAME"]
users_collection = config["USERS_COLLECTION"]
mongo_url=config["MONGO_URL"]
mongo_port=int(config["MONGO_PORT"])

# connect to MongoDB
client = pymongo.MongoClient(mongo_url, mongo_port)

# create database 
db = client[db_name]

# create collection
users = db[users_collection]

# insert document
users.insert_one(
{
    "username": "NicK",
    "full_name": "Nicolas",
    "email": "nicolas@email.com",
    "hashed_password": "$2b$12$RbAOUFzNDykl2cNATFl0YueLjzoczb/1mFqTVrzxiErZ4UCqWifXa", # 123
    "disabled": False,
  }
)
