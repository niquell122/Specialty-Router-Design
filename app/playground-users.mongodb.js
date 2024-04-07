const database = 'SpecialtyRouterDesign';
const usersCollection = 'users';

use(database);
db.createCollection(usersCollection);


db.getCollection(usersCollection).deleteMany({})


// Mocking some users. hashes need to be real.
db.getCollection(usersCollection).insertMany([
  {
    "username": "NicK",
    "full_name": "Nicolas",
    "email": "nicolas@email.com",
    "hashed_password": "$2b$12$RbAOUFzNDykl2cNATFl0YueLjzoczb/1mFqTVrzxiErZ4UCqWifXa", // pwd: 123
    "disabled": false,
  },
  {
    "username": "johndoe",
    "full_name": "John Doe",
    "email": "johndoe@example.com",
    "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", // pwd: secret
    "disabled": false,
  }
]);

print(db.getCollection(usersCollection).countDocuments())

db.getCollection(usersCollection).find()

