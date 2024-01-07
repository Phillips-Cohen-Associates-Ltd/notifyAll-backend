from sqlalchemy import Column, String, TIMESTAMP,Integer, ForeignKey
from ..config.database import Base
from sqlalchemy.sql import func


class Country(Base):
   __tablename__ = 'country'
   id= Column(Integer, primary_key=True)
   name = Column(String(100))
   iso2= Column(String(5))
   dial_code= Column(String(10))
   countryCode = Column(String(100), primary_key=True)
   created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
   updated_at = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now()) 

class State(Base):
   __tablename__ = 'state'
   id= Column(Integer, primary_key=True)
   name = Column(String(255))
   country_id = Column(Integer, ForeignKey('country.id'))
   stateCode = Column(String(100))
   created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
   updated_at = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())


class City(Base):
   __tablename__ = 'city'
   id= Column(Integer, primary_key=True)
   name = Column(String(255))
   state_id= Column(Integer, ForeignKey('state.id'))
   country_id= Column(Integer, ForeignKey('country.id'))
   created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
   updated_at = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())   