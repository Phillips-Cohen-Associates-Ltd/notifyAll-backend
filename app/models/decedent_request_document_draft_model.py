from sqlalchemy import Column, String, Integer, Boolean, Date, Text, BigInteger, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base
from ..config.database import Base



class DecedentRequestDocumentDraft(Base):
  __tablename__ = 'decedent_request_documents_draft'

  id = Column(String(36), primary_key=True)
  request_id = Column(String(36), nullable=False)
  document = Column(String(255), nullable=False)
  status = Column(TINYINT, nullable=False, server_default='1')
  created_at = Column(TIMESTAMP, nullable=True)
  updated_at = Column(TIMESTAMP, nullable=True)
  size = Column(String(255), nullable=True)