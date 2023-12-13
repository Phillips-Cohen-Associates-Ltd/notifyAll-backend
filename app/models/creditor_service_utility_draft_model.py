from sqlalchemy import Column, String, Integer, Boolean, Date, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT
from ..config.database import Base


class CreditorServiceUtilityDraft(Base):
 __tablename__ = 'creditor_service_utility_draft'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=False)
 creditor_id = Column(String(36), nullable=False)
 asset_type = Column(String(255), nullable=False)
 is_approved = Column(TINYINT, nullable=False, default=0, comment='1= Approve, 0= Pending')
 service_number = Column(String(255), nullable=False)
 cancel = Column(TINYINT(1), nullable=False, default=1)
 data_id = Column(String(255), nullable=True)
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)