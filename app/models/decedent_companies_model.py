from sqlalchemy import Column, String, Integer, Boolean, Date, Text, BigInteger, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.mysql import  TINYINT, LONGTEXT
from ..config.database import Base


class DecedentCompanies(Base):
 __tablename__ = 'decedent_companies'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=True)
 name = Column(String(70), nullable=False)
 phone_flag_code = Column(String(5), nullable=True)
 phone_number = Column(String(20), nullable=True)
 industry_type = Column(String(50), nullable=True)
 account_number = Column(Text, nullable=True)
 is_have_more_customer = Column(TINYINT, nullable=True)
 closed_accounts_email = Column(String(50), nullable=True)
 customer_service_email = Column(String(50), nullable=True)
 other_email = Column(String(50), nullable=True)
 contact_name = Column(String(100), nullable=True)
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)
 is_approved = Column(TINYINT, nullable=False, default=0)
 customer_count = Column(BigInteger, nullable=True)
 size = Column(String(50), nullable=True)
 category = Column(String(50), nullable=True)
 industries = Column(String(255), nullable=True)
 account_type = Column(String(5), nullable=True)
 is_verified = Column(TINYINT, nullable=False, default=0, comment='0-Pending, 1-Verified')
 sf_id = Column(String(255), nullable=True)