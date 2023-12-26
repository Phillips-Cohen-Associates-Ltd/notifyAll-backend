from sqlalchemy import Column, String, Integer, Boolean, Date, Text, BigInteger, ForeignKey, TIMESTAMP, BIGINT
from sqlalchemy.dialects.mysql import TINYINT, LONGTEXT
from ..config.database import Base


class CreditorPropertyUtility(Base):
 __tablename__ = 'creditor_property_utility'

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
 transfer = Column(TINYINT, nullable=False, server_default='0')
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
 sf_id = Column(String(255), nullable=True)
 country_code = Column(String(255), nullable=True)
 delete_status = Column(BigInteger, nullable=False, server_default='0')



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


class CreditorPropertyUtilityDetailsDraft(Base):
    __tablename__ = "creditor_property_utility_details_draft"

    id = Column(String(36), primary_key=True)
    request_id = Column(String(36), nullable=False)
    creditor_id = Column(String(36), nullable=False)
    asset_type = Column(String(36), nullable=False)
    meter_read = Column(String(255), nullable=True)
    meter_read_date = Column(Date, nullable=True)
    is_approved = Column(TINYINT, nullable=False, default=0)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
    data_id = Column(String(255), nullable=True)
    dual_flag_code = Column(BIGINT, nullable=False, default=0, comment="1. Gas, 2. Electric")