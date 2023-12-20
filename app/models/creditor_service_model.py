from sqlalchemy import Column, String, Integer, Boolean, Date, TIMESTAMP, Text, BIGINT
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



class CreditorTransferDetails(Base):
 __tablename__ = 'creditor_transfer_details'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=True)
 creditor_id = Column(String(36), nullable=True)
 asset_type = Column(String(50), nullable=True)
 title = Column(String(100), nullable=True)
 full_name = Column(String(100), nullable=True)
 date_of_birth = Column(String(20), nullable=True)
 service_transferred = Column(String(255), nullable=True)
 account_or_service_number = Column(String(255), nullable=True)
 invoice_type = Column(String(50), nullable=True)
 bill_address = Column(Text, nullable=True)
 concession_type = Column(String(50), nullable=True)
 concession_number = Column(String(50), nullable=True)
 current_address = Column(Text, nullable=True)
 residential_status = Column(String(50), nullable=True)
 duration_current_address_years = Column(String(255), nullable=True)
 duration_current_address_months = Column(String(255), nullable=True)
 previous_address = Column(Text, nullable=True)
 duration_previous_address_years = Column(String(255), nullable=True)
 duration_previous_address_months = Column(String(255), nullable=True)
 occupation = Column(String(255), nullable=True)
 employer = Column(String(255), nullable=True)
 length_of_employment_years = Column(String(255), nullable=True)
 length_of_employment_months = Column(String(255), nullable=True)
 employer_phone_number = Column(String(20), nullable=True)
 previous_employer = Column(String(255), nullable=True)
 previous_length_of_employment_years = Column(String(255), nullable=True)
 previous_length_of_employment_months = Column(String(255), nullable=True)
 primary_source_of_income = Column(String(255), nullable=True)
 priority_assistance = Column(String(255), nullable=True)
 directory_listing = Column(String(255), nullable=True)
 preferred_listing_name = Column(String(255), nullable=True)
 caller_identification = Column(String(255), nullable=True)
 primary_document_type = Column(String(255), nullable=True)
 primary_document_number = Column(String(255), nullable=True)
 primary_document_expirydate = Column(String(255), nullable=True)
 secondary_document_type = Column(String(255), nullable=True)
 secondary_document_number = Column(String(255), nullable=True)
 secondary_document_expirydate = Column(String(255), nullable=True)
 irn = Column(String(255), nullable=True)
 mobile_transfer_only = Column(String(255), nullable=True)
 new_owner_signature = Column(String(255), nullable=True)
 date_signed = Column(String(255), nullable=True)
 status = Column(TINYINT, nullable=False, default=0)
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)
 delete_status = Column(BIGINT, nullable=False, default=0)

