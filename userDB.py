from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
import pymongo
from typing import List
from pydantic import BaseModel, Field
import uuid

config = dotenv_values(".env")

router = APIRouter()

uri=config["ATLAS_URI"]
db_name = config["DB_NAME"]
users_collection = config["USER_SCOLLECTION"]



client = pymongo.MongoClient(uri)
db = client[db_name]
users = db[users_collection]