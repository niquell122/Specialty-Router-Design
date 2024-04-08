# Use the official MongoDB image from the Docker Hub
FROM mongo:latest

# Copy the JSON file with the initial data into the container
COPY data/users.json data/users.json
COPY data/questions.json data/questions.json

# Start MongoDB and import the data
CMD mongoimport --host mongodb --db specialty_router_design --collection users --type json --file data/users.json --jsonArray \
    && mongoimport --host mongodb --db specialty_router_design --collection question-history --type json --file data/questions.json --jsonArray

