from sqlalchemy import Column, String, TIMESTAMP
from ..config.database import Base
from sqlalchemy.sql import func


class Country(Base):
   __tablename__ = 'countries'
   name = Column(String(100))
   isoCode = Column(String(100))
   countryCode = Column(String(100), primary_key=True)
   created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
   updated_at = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())

class State(Base):
   __tablename__ = 'states'
   name = Column(String(255), primary_key=True)
   isoCode = Column(String(100))
   countryCode = Column(String(100))
   created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
   updated_at = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())

class City(Base):
   __tablename__ = 'cities'
   name = Column(String(255))
   countryCode = Column(String(100))
   stateCode = Column(String(100), primary_key=True)
   created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
   updated_at= Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())