
# Security
SECRET_KEY = "your_secret_key_here"
AUTH_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 999

# Fake database
fake_users_db = {
    "NicK": {
        "username": "NicK",
        "full_name": "Nick Niquell",
        "email": "niquellNick@example.com",
        "hashed_password": "$2b$12$kLOUo76wuwIU6994II8FFukVfwzbEAocqPW27kfMzYho9AGfjYMjO",  # password is "secret"
        "disabled": False,
    }
}
