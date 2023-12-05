from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config.config import settings

# SQLITE_DATABASE_URL = "mysql://root:00000@127.0.0.1/fastapi"

SQLITE_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}/{settings.POSTGRES_DB}"
# engine = create_engine(
#     SQLITE_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
# )
engine = create_engine(SQLITE_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
