from sqlalchemy import Column, String
from ..config.database import Base


class Country(Base):
   __tablename__ = 'countries'
   name = Column(String)
   isoCode = Column(String)
   countryCode = Column(String, primary_key=True)

class State(Base):
   __tablename__ = 'states'
   name = Column(String)
   isoCode = Column(String)
   countryCode = Column(String, primary_key=True)

class City(Base):
   __tablename__ = 'cities'
   name = Column(String)
   countryCode = Column(String, primary_key=True)
   stateCode = Column(String, primary_key=True)