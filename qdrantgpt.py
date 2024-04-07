from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from gpt import client as gpt_client
from datetime import datetime
from mongodb_question_history import question_history
from dotenv import dotenv_values

config = dotenv_values(".env")

qdrant_url=config["QDRANT_URL"]
col=config["QDRANT_COLLECTION"]

qclient = QdrantClient(url=qdrant_url)


def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return gpt_client.embeddings.create(input = [text], model=model).data[0].embedding

def add_question_with_context(index: int, question: str, context: str):
   embedding = get_embedding(question)
   if not index:
     index = int(datetime.now().strftime("%Y%m%d%H%M%S"))
   qclient.upsert(
        collection_name=col,
        wait=True,
        points=[
            PointStruct(id=index, vector=embedding, payload={ "question": question, "context": context})
    ],
)
   
def get_question_context(username, question):
    new_embedding = get_embedding(question)

    question_history.insert_one({
       "user": username,
       "question": question,
       "timestamp": datetime.now(),
       "chat_id":"one day maybe" 
    })

    search_result = qclient.search(
    collection_name=col, query_vector=new_embedding, limit=3
    )
    first_match = search_result[0]
    context = first_match.payload["context"]

    return context

