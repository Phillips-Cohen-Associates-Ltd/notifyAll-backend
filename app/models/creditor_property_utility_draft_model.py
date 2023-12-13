from sqlalchemy import Column, String, Integer, Boolean, Date, TIMESTAMP
from sqlalchemy.dialects.mysql import  TINYINT
from ..config.database import Base


class CreditorPropertyUtilityDraft(Base):
 __tablename__ = 'creditor_property_utility_draft'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=False)
 creditor_id = Column(String(36), nullable=False)
 asset_type = Column(String(36), nullable=False)
 first_name_old = Column(String(255), nullable=True)
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)
 last_name_old = Column(String(255), nullable=True)
 email_old = Column(String(255), nullable=True)
 phone_old = Column(String(255), nullable=True)
 address_old = Column(String(255), nullable=True)
 first_name_new = Column(String(255), nullable=True)
 last_name_new = Column(String(255), nullable=True)
 email_new = Column(String(255), nullable=True)
 phone_new = Column(String(255), nullable=True)
 other_notifier_flag_code = Column(String(5), nullable=True)
 address_new = Column(String(255), nullable=True)
 transfer = Column(TINYINT(1), nullable=False, default=0, comment='0 - cancel,1 - transfer')
 country_new_account = Column(String(255), nullable=True)
 state_new_account = Column(String(255), nullable=True)
 city_new_account = Column(String(255), nullable=True)
 zip_code_new = Column(String(255), nullable=True)
 country_old_account = Column(String(255), nullable=True)
 state_old_account = Column(String(255), nullable=True)
 city_old_account = Column(String(255), nullable=True)
 zip_code_old = Column(String(255), nullable=True)
 transfer_to = Column(String(255), nullable=True)
 data_id = Column(String(255), nullable=True)
 country_code = Column(String(255), nullable=True)