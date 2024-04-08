from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from gpt import client as gpt_client
from datetime import datetime
from mongodb_question_history import question_history
from dotenv import dotenv_values
from uuid import uuid4
from collections import Counter

config = dotenv_values(".env")

qdrant_url=config["QDRANT_URL"]
col=config["QDRANT_COLLECTION"]
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

def get_question_context(username, question, limit=3):
   new_embedding = get_embedding(question)

   question_history.insert_one({
   "user": username,
   "question": question,
   "timestamp": datetime.now(),
   "chat_id":"one day maybe" 
   })

   search_result = qclient.search(
   collection_name=col, query_vector=new_embedding, limit=limit
   )
   first_match = search_result[0]

   if first_match.score > 0.9:
      return first_match.payload["context"]

   context, ammount = get_majority(search_result, "context")

   if(ammount>majority_threshold):
      return context
   
   return {"Hal":"i'm sorry Dave, I'm affraid i can't do that."}

