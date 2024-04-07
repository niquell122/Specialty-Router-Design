from qdrant_client.models import Distance, VectorParams
import mocks
from qdrantgpt import qclient, add_question_with_context, col, get_embedding


try:
    operation_info = qclient.get_collection(collection_name=col)
    operation_info = qclient.delete_collection(collection_name=col)
    print("\ncollection deleted")
except:
    print("\ncollection not found.")


operation_info= qclient.create_collection(
    collection_name=col,
    vectors_config=(VectorParams(size=1536, distance=Distance.COSINE)))

if(operation_info):
    print("create_collection: " + str(operation_info))
   

question_context = mocks.mock_question_context

if (question_context):
    for i in range(len(question_context)):
        dict = question_context[i]
        print(dict)
        add_question_with_context(index=i, question=dict["phrase"], context=dict["context"] )


new_question="como faz para transferir dinhero?"
new_embedding = get_embedding(new_question)

# print('\nNew Embedding:')
# print(new_embedding[:5])

search_result = qclient.search(
    collection_name=col, query_vector=new_embedding, limit=3
)

print('\nNew Question:')
print(new_question)

print('\nSearch Result:')
for sr in search_result:
   print(sr.payload)

