const database = 'SpecialtyRouterDesign';
const usersCollection = 'question-history';

use(database);
db.createCollection(usersCollection);

// // clearing database
db.getCollection(usersCollection).deleteMany({})


// // Mocking some data.
// db.getCollection(usersCollection).insertMany([
//   {
//     "user": "Some Random Guys",
//     "question": "His question",
//     "timestamp": Date.now(),
//     "chat_id":"one day maybe" 
//   }
// ]);

print(db.getCollection(usersCollection).countDocuments())

db.getCollection(usersCollection).find()

