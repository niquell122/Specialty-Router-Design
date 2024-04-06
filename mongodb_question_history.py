from fastapi import APIRouter
from dotenv import dotenv_values
import pymongo

config = dotenv_values(".env")

router = APIRouter()

uri=config["ATLAS_URI"]
db_name = config["DB_NAME"]
users_collection = config["QUESTION_HISTORY_COLLECTION"]



client = pymongo.MongoClient(uri)
db = client[db_name]
question_history = db[users_collection]
