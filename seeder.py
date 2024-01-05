from sqlalchemy import create_engine, MetaData, Column, Integer, Numeric, String, Date, Table, ForeignKey
from faker import Faker
import sys
from uuid import uuid4
from app.service.hashing import Hasher 
from datetime import datetime
from app.config.config import settings

metadata= MetaData()
faker= Faker()


# Set up connection between sqlalchemy and postgres dbapi
engine = create_engine(f"mysql+mysqlconnector://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}/{settings.POSTGRES_DB}")
# "mysql+mysqlconnector://root:kishore12@127.0.0.1/notifyAll"
# Create a metadata object
with engine.connect() as conn:
    metadata.reflect(conn)

users = metadata.tables['users']

class GenerateData:
    """
    generate a specific number of records to a target table in the
    postgres database.
    """
    
    def __init__(self):
        """
        define command line arguments.
        """
        self.table = sys.argv[1]
        self.num_records = int(sys.argv[2]) # Add this line

    def create_data(self):
        if self.table == "users":
           with engine.begin() as conn:
              for _ in range(self.num_records):
                 insert_stmt = users.insert().values(
                  id=str(uuid4()),
                  name=faker.name(),
                  email=faker.unique.email(),
                  password=Hasher.get_password_hash("pass"),
                  is_approved=faker.boolean(),
                  is_email_verified=faker.boolean(),
                  verification_code=faker.bothify(text='?????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'),
                  created_at=datetime.utcnow(),
                  updated_at=datetime.utcnow())
                 conn.execute(insert_stmt)

if __name__ == "__main__":    
    generate_data = GenerateData()   
    generate_data.create_data()