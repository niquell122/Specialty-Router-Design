from fastapi import FastAPI
from auth import router as auth_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the SPECIAL ROUTER DESIGN Test from NicK!"}




app.include_router(auth_router)