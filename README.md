# Specialty Router Design

This application aims at looking for the ideal context given a end-users input, written in common language. To that end we use the gpt embedding tools to find a ammount of phrases in our database that are the closest to the user input. That comparison is made between the embedding of the the user input and the embeddings for our phrases stored in our Qdrant database. After finding the closest phrases we can consider:
-  Return the context for the closest match, if it passes a threshold of similarity.
-  Return the most present context in the search result, if  most (>7) of the results bellong to the same context.
-  Include the user recent history of questions and redo the search.
-  Give up and admit we can't find a context for that input.

## Technologies
### Qdrant Database:
The phrases we already know are saved (besides their embeddings) in a Qdrant Vector Database. This database provide means to store, fetch and compare embeddings extremely fast. The comparisons between embeddings are made using Cosine Similarity, often used with text to compare how similar two documents or sentences are to each other, and returns a number in range [-1, 1] that we can use to determine not just the closest phrase to the user input, but how close they are, in a way we can determine a threshold (0.9 in the current build) that the result should pass before deciding that the context for the closest match is good enough and return.

for more info: https://qdrant.tech/documentation/overview/

### MongoDB:
User history is stored in mongodb for easy and efficient access and flexible payload.

```json
{
  "_id": {
    "$oid": "66142e7407619efc3bb2cdde"
  },
  "user": "NicK",
  "question": "como faço um pix?",
  "timestamp": {
    "$date": "2024-04-08T16:50:44.209Z"
  },
  "chat_id": "2637827407619efc3bb2cde"
}
``` 
This history is used latter in case the current user input is not enought to determine the context of his phrase.


### OPENAI GPT:
GPT is the easiest and most reliable way to generate embeddings for the user input as well as for the phrases in our database. Those embeddings are numeric representations of the text the user inputs and the phrases we hold in our database and can be compared to fetch the closest pre registered phrase(s) in our database to that of the common language used in the user input.

## Start-up:

> $ docker-compose up

All tests should be done using the Swagger Document page at:
http://localhost:8000/docs


## NOTE: <br>
> at the docker-compose file, set the OPENAI_API_KEY value for the 2 relevant containers.


### Authentication:
> username: NicK <br>
> password: 123

##### * the username has upercases N and K: NicK


## Endpoints:

#### GET '/'
Mainpage, just a hello-world-like page.

#### POST '/token'
Used for authentication with the fast-api security lib.
* Instead of authenticating from this endpoint, try the Authorize button on the Swagger page.


#### POST '/question/context'
This is the main focus of this application.
All requests from POST 'question/context' are being saved on the question_history database @mongodb.
It takes a question a runs agains the Qdrant database to chose the best suited context for that question.
The 2 possible contexts are: PIX and BOLETO.
Deciding on the best result:
- If a question has more then 0.9 similarity to any specific entry in the Qdrant database
 (compared using gpt embeddings), the application will return the context related to that specific entry.
- If a question doesn't match any entry in the database at more then 0.9 similarity, the application return the 10 closest entries.
- If most (more then 7) of the results retrieved belong to the same context, the application will return that context.
At this point, if previous steps failed, the application will look for recent activity from the user and try to match his previous+current message.
- If the history doesn't help, a failing message is returned. (we can consider updating our databse with a new entry at this point. RAG?)