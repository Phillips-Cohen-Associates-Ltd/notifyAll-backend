from sqlalchemy import Column, String, Integer, Boolean, Date, Text, BigInteger, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from ..config.database import Base



class DecedentRequestCreditor(Base):
 __tablename__ = 'decedent_request_creditors'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=False)
 creditor_id = Column(String(36), nullable=False)
 asset_type = Column(String(255), nullable=False)
 account_number = Column(LONGTEXT, nullable=False)
 meter_read = Column(String(255), nullable=True)
 meter_read_date = Column(String(255), nullable=True)
 is_approved = Column(TINYINT, nullable=False, server_default='0')
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)
 data_id = Column(String(255), nullable=True)
 delete_status = Column(BigInteger, nullable=False, server_default='0')