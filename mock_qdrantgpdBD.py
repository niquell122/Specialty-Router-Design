from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from qdrantgpt import qclient, add_question_with_context, col, get_embedding
from qdrant_client import QdrantClient
from dotenv import dotenv_values
import mocks
config = dotenv_values(".env")
from datetime import datetime

qdrant_url="http://localhost:6333"
col=config["QDRANT_COLLECTION"]

qclient = QdrantClient(url=qdrant_url)
question_context = mocks.mock_question_context

def add_question_with_context(index: int, question: str, context: str):
   embedding = get_embedding(question)
   if not index:
     index = int(datetime.now().strftime("%Y%m%d%H%M%S"))
   status = qclient.upsert(
        collection_name=col,
        wait=True,
        points=[
            PointStruct(id=index, vector=embedding, payload={ "question": question, "context": context})
    ],
   )
   print(f'Upsert: {status}')

try:
    # collection is already started
    operation_info = qclient.get_collection(collection_name=col)
    print(f'Get Collection: {operation_info}')

except:
    # start collection
    print('STARTING COLLECTION')
    operation_info= qclient.create_collection(
    collection_name=col,
    vectors_config=(VectorParams(size=1536, distance=Distance.COSINE))
    )

    # populate collection
    for i in range(len(question_context)):
        dict = question_context[i]
        add_question_with_context(index=i, question=dict["phrase"], context=dict["context"] )

# new_question="como transferir dinhero?"
# new_embedding = get_embedding(new_question)

# search_result = qclient.search(
#     collection_name=col, query_vector=new_embedding, limit=3
# )

# print(search_result)
