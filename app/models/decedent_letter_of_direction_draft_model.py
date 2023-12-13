from sqlalchemy import Column, String, Integer, Boolean, Date, Text, BigInteger, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.mysql import  TINYINT, LONGTEXT
from ..config.database import Base


class DecedentLetterOfDirections(Base):
 __tablename__ = 'decedent_letter_of_directions'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=True)
 recipient = Column(String(255), nullable=True)
 contact_type = Column(String(255), nullable=True)
 destination = Column(String(255), nullable=True)
 subject = Column(String(255), nullable=True)
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)