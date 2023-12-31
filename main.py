from app.models import user_model
from app.routes import commonroutes, userroute, notifierroutes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import engine

user_model.Base.metadata.create_all(bind=engine)

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
app.include_router(commonroutes.router, tags=['Countries'], prefix='/api')
app.include_router(notifierroutes.router, tags=['NotifierInformation'], prefix='/api')


# app.include_router(chatroute.router, tags=['Chat'], prefix='/chatbot')

@app.get("/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}
