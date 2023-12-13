from sqlalchemy import Column, String, Integer, Boolean, Date, Text, BigInteger, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, TINYINT, LONGTEXT
from ..config.database import Base


class CreditorPropertyUtilityDetail(Base):
 __tablename__ = 'creditor_property_utility_details'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=False)
 creditor_id = Column(String(36), nullable=False)
 asset_type = Column(String(36), nullable=False)
 meter_read = Column(String(255), nullable=True)
 meter_read_date = Column(Date, nullable=True)
 is_approved = Column(TINYINT, nullable=False, server_default='0')
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)
 data_id = Column(String(255), nullable=True)
 delete_status = Column(BigInteger, nullable=False, server_default='0')
 dual_flag_code = Column(BigInteger, nullable=False, server_default='0')