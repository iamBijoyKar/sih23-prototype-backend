from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from model import User, Item


app = FastAPI()
session = SessionLocal()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    que = session.query(User).all()
    print(que)
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app)