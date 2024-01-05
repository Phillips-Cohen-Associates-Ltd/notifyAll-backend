# from app.models import user_model
from app.routes import commonroutes, userroute, notifierroutes
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import engine
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


# user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
   return JSONResponse(
       status_code=422,
       content={"message": "Not Accepted"},)

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
