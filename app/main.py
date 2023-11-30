from app.models import usermodel
from app.routes import userroute
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.database import engine

usermodel.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:4200",
    "http://localhost:4202"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(userroute.router, tags=['Users'], prefix='/api')
# app.include_router(chatroute.router, tags=['Chat'], prefix='/chatbot')

@app.get("/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}
