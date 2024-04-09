from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from qdrant_gpt import qclient, add_question_with_context, col, get_embedding
from qdrant_client import QdrantClient
from dotenv import dotenv_values
from gpt import client as gpt_client
import mocks
config = dotenv_values(".env")
from uuid import uuid4

col=config["QDRANT_COLLECTION"]
model=config["EMBEDDING_MODEL"]

# qdrant to run from inside a docker container
# ↖qdrant is the name of the image inside docker-compose)
# localhost to run locally
qdrant_url="http://qdrant:6333"

qclient = QdrantClient(url=qdrant_url)
question_context = mocks.mock_question_context

try:
    # see if collection is already started
    qclient.get_collection(collection_name=col)
    # print(f'Get Collection: {operation_info}')
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
        data = dict["data"]
        context = dict["context"]
        embedding = get_embedding(data)

        text = data.replace("\n", " ")
        gpt_client.embeddings.create(input = [text], model=model).data[0].embedding

        index = str(uuid4())
        
        qclient.upsert(
            collection_name=col,
            wait=True,
            points=[
                PointStruct(id=index, vector=embedding, payload={ "data": data, "context": context})
            ],
        )

# # Can run Manual Tests here:
# new_question="Quais são os horários de funcionamento do PIX?'?"
# new_embedding = get_embedding(new_question)

# search_result = qclient.search(
#     collection_name=col, query_vector=new_embedding, limit=10
# )

# # print(search_result)
# print('Result Payload: ')
# for r in search_result:
#    print(r)

