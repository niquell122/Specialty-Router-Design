from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from gpt import client as gpt_client
from datetime import datetime, timedelta
from mongodb_question_history import question_history
from dotenv import dotenv_values
from uuid import uuid4
from collections import Counter

config = dotenv_values(".env")

qdrant_url=config["QDRANT_URL"]
col=config["QDRANT_COLLECTION"]
search_quantity=int(config["SEARCH_QUANTITY"])
score_threshold=float(config["SCORE_THRESHOLD"])

majority_threshold=int(config["MAJORITY_THRESHOLD"])

qclient = QdrantClient(url=qdrant_url)

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return gpt_client.embeddings.create(input = [text], model=model).data[0].embedding

def add_question_with_context(index: int, data: str, context: str):
   embedding = get_embedding(data)
   if not index:
      index = int(uuid4())
      qclient.upsert(
         collection_name=col,
         wait=True,
         points=[
            PointStruct(id=index, vector=embedding, payload={ "data": data, "context": context})
      ],
   )
      
def get_majority(list, fieldname):
   field_counts = Counter([item.payload[fieldname] for item in list])
   most_common_value = field_counts.most_common(1)[0][0]
   number_of_appearances = field_counts.most_common(1)[0][1]
   return most_common_value, number_of_appearances

def get_question_context(username, data, limit=search_quantity, history=True):
   new_embedding = get_embedding(data)
   question_history.insert_one({
   "user": username,
   "data": data,
   "timestamp": datetime.now(),
   "chat_id":"one day maybe" 
   })

   search_result = qclient.search(
   collection_name=col, query_vector=new_embedding, limit=limit
   )
   first_match = search_result[0]

   # return if the match score is higher then the threshold:
   if first_match.score >= score_threshold:
      return first_match.payload["context"]

   majority_context, ammount = get_majority(search_result, "context")

   # return if the result has a numer of objects of the same context higher then the threshold
   if(ammount>majority_threshold):
      return majority_context
   
   # if history is set, check users history
   if(history):
      two_minutes_ago = datetime.now() - timedelta(minutes=2)
      user_recent_history=question_history.find({
         "user": username,
         "timestamp": {
            "$gte": two_minutes_ago,
         },
         "data": {
            "$ne": data
         }
      })
      # if the user has 
      if(user_recent_history):
         for previous_message in user_recent_history:
            data+=previous_message["data"]

         return get_question_context(
            username=username, 
            data=data,
            limit=search_quantity,
            history=False
         )
   
   # give up
   return {"Hal":"i'm sorry Dave, I'm affraid i can't do that."}

