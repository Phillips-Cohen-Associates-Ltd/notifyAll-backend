from sqlalchemy import Column, String, Integer, Boolean, Date, Text, BigInteger, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.mysql import TINYINT, LONGTEXT
from ..config.database import Base


class DecedentMembershipAccountDraft(Base):
 __tablename__ = 'decedent_membership_account_draft'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=True)
 aeroplan_from = Column(String(255), nullable=True)
 aeroplan_to = Column(String(255), nullable=True)
 airmiles_from = Column(String(255), nullable=True)
 airmiles_to = Column(String(255), nullable=True)
 cancel_ama = Column(String(255), nullable=True)
 petropoints_from = Column(String(255), nullable=True)
 petropoints_to = Column(String(255), nullable=True)
 sobeys_from = Column(String(255), nullable=True)
 sobeys_to = Column(String(255), nullable=True)
 blue_cross = Column(String(255), nullable=True)
 driver_lic_photo = Column(String(255), nullable=True)
 nexus = Column(String(255), nullable=True)
 ahcip_account = Column(String(255), nullable=True)
 indigenous_service = Column(String(255), nullable=True)
 death_of_canadian_armed = Column(String(255), nullable=True)
 death_of_federal = Column(String(255), nullable=True)
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)