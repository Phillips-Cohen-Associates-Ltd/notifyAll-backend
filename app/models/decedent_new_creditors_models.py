from sqlalchemy import Column, String, Integer, Boolean, Date, Text, BigInteger, ForeignKey, TIMESTAMP, ForeignKeyConstraint
from sqlalchemy.dialects.mysql import  TINYINT, LONGTEXT
from sqlalchemy.orm import relationship
from ..config.database import Base



class DecedentNewCreditor(Base):
 __tablename__ = 'decedent_new_creditors'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=False)
 creditor_id = Column(String(36), nullable=True)
 decedent_company_id = Column(String(36), nullable=True)
 name = Column(String(255), nullable=False)
 country_id = Column(BigInteger, nullable=True)
 address = Column(String(255), nullable=True)
 state = Column(String(50), nullable=True)
 city = Column(String(50), nullable=True)
 zipcode = Column(String(8), nullable=True)
 email = Column(String(255), nullable=True)
 phone_flag_code = Column(String(5), nullable=True)
 phone_number = Column(String(255), nullable=True)
 country_code = Column(String(255), nullable=True)
 asset_type = Column(String(255), nullable=True)
 account_number = Column(LONGTEXT, nullable=True)
 is_admin_alert_mail_sent = Column(TINYINT, nullable=False, server_default='0')
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)
 industry_type = Column(String(50), nullable=True)
 is_have_more_customer = Column(TINYINT, nullable=True)
 closed_accounts_email = Column(String(50), nullable=True)
 customer_service_email = Column(String(50), nullable=True)
 other_email = Column(String(50), nullable=True)
 contact_name = Column(String(100), nullable=True)
 is_approved = Column(TINYINT, nullable=False, server_default='0')
 is_paid = Column(TINYINT, nullable=True, server_default='0')
 decedent_request_payment_id = Column(String(36), nullable=True)
 is_new = Column(TINYINT, nullable=True, server_default='1')
 follow_up_no_response_count = Column(String(255), nullable=False, server_default='0')
 email_sent_at = Column(TIMESTAMP, nullable=True)
