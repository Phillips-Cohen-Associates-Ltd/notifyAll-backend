from sqlalchemy import Column, String, Integer, Boolean, Date, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT, BIGINT
from ..config.database import Base


class CreditorServiceUtility(Base):
 __tablename__ = 'creditor_service_utility'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=False)
 creditor_id = Column(String(36), nullable=False)
 asset_type = Column(String(255), nullable=False)
 is_approved = Column(TINYINT, nullable=False, default=0, comment='1= Approve, 0= Pending')
 service_number = Column(String(255), nullable=False)
 cancel = Column(TINYINT(1), nullable=False, default=1)
 data_id = Column(Integer, nullable=False, default=0)
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)
 delete_status = Column(BIGINT, nullable=False, default=0, comment='0. Active Data, 1. Deleted Data')