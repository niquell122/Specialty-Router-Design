from fastapi import APIRouter
from dotenv import dotenv_values
import pymongo

config = dotenv_values(".env")

router = APIRouter()

db_name = config["DB_NAME"]
question_history_collection = config["QUESTION_HISTORY_COLLECTION"]
mongo_url=config["MONGO_URL"]
mongo_port=int(config["MONGO_PORT"])


# connect to MongoDB
client = pymongo.MongoClient(mongo_url, mongo_port)

# create database
db = client[db_name]

# create collection
question_history = db[question_history_collection]
