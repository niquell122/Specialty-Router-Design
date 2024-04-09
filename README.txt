Start-up:

> $ docker-compose up

All tests should be done using the Swagger Document page at:
http://localhost:8000/docs



FIRST: at the docker-compose file, set the OPENAI_API_KEY value for the 2 relevant containers.


Authentication:
User:
    username: NicK
    password: 123

* the username has upcasts N and K -> NicK


Endpoints:

GET '/'
Mainpage, just a hello-world-like page.

POST 'token'
Used for authentication with the fast-api security lib.
* Instead of authenticating from this endpoints, try the Authorize button on the Swagger page.


POST 'question/context'
This is the main focus of this application.
All requests from POST 'question/context' are being saved on the question_history database @mongodb.
It takes a question a runs agains the Qdrant database to chose the best suited context for that questio.
The 2 possible contexts are: PIX and BOLETO
If a question has more then 0.9 similarity to any specific entry in the Qdrant database
 (compared using gpt embeddings), the application will return the context related to that specific entry.
If a question doesn't match any entry in the database at more then 0.9 similarity, the application return the 10 closest entries.
If most (more then 7) of the results retrieved belong to the same context, the application will return that context.
At this point, if previous steps failed, the application will look for recent activity from the user and try to match his previous+current message.
If the history doesn't help, a failing message is returned.