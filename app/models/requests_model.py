from sqlalchemy import Column, String, Integer, Boolean, Date, Text, BigInteger, ForeignKey, TIMESTAMP, DateTime, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, TINYINT, LONGTEXT
from sqlalchemy.sql import func
from uuid import uuid4
from ..config.database import Base
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE



class DecedentRequest(Base):
   __tablename__ = 'decedent_requests'
   id = Column(String(36), primary_key=True)
   user_id = Column(String(36), nullable=True)
   funeral_home_id = Column(String(36), nullable=True)
   notifier_salutation = Column(String(5), nullable=True)
   name = Column(String(50), nullable=False)
   middle_name = Column(String(50), nullable=True)
   last_name = Column(String(50), nullable=True)
   address = Column(Text, nullable=True)
   address_two = Column(Text, nullable=True)
   email = Column(String(50), nullable=True)
   apartment= Column(String(50))

   phone_number = Column(String(20), nullable=True)
   relationship = Column(String(40), nullable=False)
   person_dealing_with_estate = Column(TINYINT(1), nullable=False)
   person_dealing_name = Column(String(50), nullable=True)
   person_dealing_phone_number = Column(String(20), nullable=True)
   probate_applied = Column(TINYINT(1), nullable=False)
   is_there_is_will = Column(TINYINT(1), nullable=False, server_default='1')
   email_available_for_contact = Column(TINYINT(1), nullable=True)
   phone_number_available_for_contact = Column(TINYINT(1), nullable=True)
   mail_available_for_contact = Column(TINYINT(1), nullable=True)
   is_verify_identity = Column(String(5), nullable=False)
   # Identity_type= Column(String(40))
   # Identity_number= Column(Integer)
   deceased_salutation = Column(String(5), nullable=True)
   first_name_of_departed = Column(String(50), nullable=True)
   middle_name_of_departed = Column(String(50), nullable=True)
   last_name_of_departed = Column(String(50), nullable=True)
   decedent_first_name = Column(String(50), nullable=True)
   decedent_last_name = Column(String(50), nullable=True)
   proof_of_death = Column(String(255), nullable=True)
   present_address = Column(Text, nullable=True)
   present_address_two = Column(Text, nullable=True)
   previous_address = Column(Text, nullable=True)
   previous_address_two = Column(Text, nullable=True)
   second_previous_address = Column(Text, nullable=True)
   second_previous_address_two = Column(Text, nullable=True)
   third_previous_address = Column(Text, nullable=True)
   third_previous_address_two = Column(Text, nullable=True)
   date_of_birth = Column(Date, nullable=True)
   date_of_death = Column(Date, nullable=True)
   date_of_death_fromdate = Column(Date, nullable=True)
   date_of_death_todate = Column(Date, nullable=True)
   cause_of_death = Column(LONGTEXT, nullable=True)
   certificate_id = Column(String(36), nullable=True)
   certificate_number = Column(String(50), nullable=True)
   acr_no = Column(String(50), nullable=True)
   reg_year = Column(String(50), nullable=True)
   ssn_number = Column(LONGTEXT, nullable=True)
   status = Column(BigInteger, nullable=False, server_default='1')
   created_at =Column(TIMESTAMP(timezone=True),nullable=False, server_default=func.now())
   updated_at = Column(TIMESTAMP(timezone=True),default=None, onupdate=func.now())
   country_code = Column(String(5), nullable=False)
   phone_flag_code = Column(String(5), nullable=True)
   person_dealing_country_code = Column(String(5), nullable=True)
   person_dealing_phone_flag_code = Column(String(5), nullable=True)
   request_id = Column(String(50), nullable=True)
   identification_id = Column(String(36), nullable=False)
   id_number = Column(String(30), nullable=False)
   import_by = Column(String(36), nullable=True)
   cause_of_death_others = Column(String(50), nullable=True)
   certificate_others = Column(String(50), nullable=True)
   identification_others = Column(String(50), nullable=True)
   debt_manager_id = Column(String(50), nullable=True)
   city = Column(Integer, nullable=True)
   state = Column(Integer, nullable=True)
   country = Column(Integer, nullable=True)
   zipcode = Column(String(10), nullable=True)
   present_city = Column(Integer, nullable=True)
   present_state = Column(Integer, nullable=True)
   present_country = Column(Integer, nullable=True)
   present_zipcode = Column(String(10), nullable=True)
   previous_city = Column(Integer, nullable=True)
   previous_state = Column(Integer, nullable=True)
   previous_country= Column(Integer, nullable=True)
   previous_zipcode = Column(String(10), nullable=True)
   previous_zipcode = Column(String(10), nullable=True)
   second_previous_city = Column(Integer, nullable=True)
   second_previous_state = Column(Integer, nullable=True)
   second_previous_country = Column(Integer, nullable=True)
   second_previous_zipcode = Column(String(10), nullable=True)
   third_previous_city = Column(Integer, nullable=True)
   third_previous_state = Column(Integer, nullable=True)
   third_previous_country = Column(Integer, nullable=True)
   third_previous_zipcode = Column(String(10), nullable=True)
   scrapper_id = Column(String(36), nullable=True)
   request_from = Column(Integer, nullable=False, server_default='1')
   excel_status = Column(Integer, nullable=False, server_default='0')
   address_type = Column(String(50), nullable=True)
   vacating_date = Column(LONGTEXT, nullable=True)
   is_spouse = Column(TINYINT(1), nullable=True, server_default='0')
   spouse_date_of_birth = Column(Date, nullable=True)
   spouse_sin = Column(String(50), nullable=True)
   spouse_first_name = Column(String(50), nullable=True)
   spouse_middle_name = Column(String(50), nullable=True)
   spouse_last_name = Column(String(50), nullable=True)
   spouse_phone_flag_code = Column(String(5), nullable=True)
   spouse_phone_number = Column(String(25), nullable=True)
   deceased_persons_phone_country_code = Column(String(5), nullable=True)
   deceased_persons_phone_flag = Column(String(5), nullable=True)
   deceased_persons_phone_number = Column(String(20), nullable=True)
   deceased_persons_sex = Column(String(20), nullable=True)
   deceased_persons_marital_status = Column(String(20), nullable=True)
   deceased_persons_country = Column(String(50), nullable=True)
   deceased_persons_state = Column(String(50), nullable=True)
   deceased_persons_citizenship = Column(String(50), nullable=True)
   signature = Column(Text, nullable=True)
   request_status = Column(BigInteger, nullable=False, server_default='1')
   sf_id = Column(String(255), nullable=True)
   
class DecedentRequestsDraft(Base):
   __tablename__ = 'decedent_requests_draft'
   
   id = Column(String(100), primary_key=True)
   user_id = Column(String(36), nullable=False)
   funeral_home_id = Column(String(36))
   notifier_salutation = Column(String(5))
   name = Column(String(50))
   middle_name = Column(String(50))
   last_name = Column(String(50))
   address = Column(Text)
   address_two = Column(Text)
   email = Column(String(50))
   phone_number = Column(String(20))
   relationship = Column(String(40))
   person_dealing_with_estate = Column(Boolean)
   person_dealing_name = Column(String(50))
   person_dealing_phone_number = Column(String(20))
   probate_applied = Column(Boolean)
   is_there_is_will = Column(Boolean, default=True)
   available_for_contact = Column(Boolean)
   email_available_for_contact = Column(Boolean)
   phone_number_available_for_contact = Column(Boolean)
   mail_available_for_contact = Column(Boolean)
   is_verify_identity = Column(String(5))
   deceased_salutation = Column(String(5))
   first_name_of_departed = Column(String(50))
   middle_name_of_departed = Column(String(50))
   last_name_of_departed = Column(String(50))
   decedent_first_name = Column(String(50))
   decedent_last_name = Column(String(50))
   proof_of_death = Column(String(255))
   present_address = Column(Text)
   present_address_two = Column(Text)
   previous_address = Column(Text)
   previous_address_two = Column(Text)
   second_previous_address = Column(Text)
   second_previous_address_two = Column(Text)
   third_previous_address = Column(Text)
   third_previous_address_two = Column(Text)
   date_of_birth = Column(String(255))
   date_of_death = Column(String(255))
   cause_of_death = Column(String(50))
   certificate_id = Column(String(36))
   certificate_number = Column(String(50))
   ssn_number = Column(Text)
   status = Column(Integer, default=1)
   created_at = Column(DateTime)
   updated_at = Column(DateTime)
   deleted_at = Column(DateTime)
   country_code = Column(String(5))
   phone_flag_code = Column(String(5))
   person_dealing_country_code = Column(String(5))
   person_dealing_phone_flag_code = Column(String(5))
   request_stage = Column(Integer, default=1)
   is_admin_updated = Column(String(5), default='0')
   identification_id = Column(String(36), nullable=False)
   id_number = Column(String(30), nullable=False)
   city = Column(Integer)
   state = Column(Integer)
   country = Column(Integer)
   zipcode = Column(String(10))
   present_city = Column(Integer)
   present_state = Column(Integer)
   present_country = Column(Integer)
   present_zipcode = Column(String(10))
   previous_city = Column(Integer)
   previous_state = Column(Integer)
   previous_country = Column(Integer)
   previous_zipcode = Column(String(10))
   second_previous_city = Column(Integer)
   second_previous_state = Column(Integer)
   second_previous_country = Column(Integer)
   second_previous_zipcode = Column(String(10))
   third_previous_city = Column(Integer)
   third_previous_state = Column(Integer)
   third_previous_country = Column(Integer)
   third_previous_zipcode = Column(String(10))
   address_type = Column(String(50))
   vacating_date = Column(String(255))
   is_spouse = Column(Boolean, default=False)
   spouse_date_of_birth = Column(DateTime)
   spouse_sin = Column(String(50))
   spouse_first_name = Column(String(50))
   spouse_middle_name = Column(String(50))
   spouse_last_name = Column(String(50))
   spouse_phone_flag_code = Column(String(5))
   spouse_phone_number = Column(String(25))
   deceased_persons_phone_country_code = Column(String(5))
   deceased_persons_phone_flag = Column(String(5))
   deceased_persons_phone_number = Column(String(20))
   deceased_persons_sex = Column(String(20))
   deceased_persons_marital_status = Column(String(20))
   deceased_persons_country = Column(String(50))
   deceased_persons_state = Column(String(50))
   deceased_persons_citizenship= Column(String(50))
   signature= Column(Text)
   step= Column(Integer)
   sf_id= Column(String(100))


class DecedentRequestDocument(Base):
    __tablename__ = "decedent_request_document"

    id = Column(String(36), primary_key=True, default=str(uuid4()))
    request_id = Column(String(36), ForeignKey("decedent_requests.id"), nullable=False)
    document = Column(String(255), nullable=False)
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())
    size = Column(String(255), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint(id, request_id),
    )


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


class DecedentRequestCreditorDraft(Base):
 __tablename__ = 'decedent_request_creditors_draft'

 id = Column(String(36), primary_key=True)
 request_id = Column(String(36), nullable=False)
 creditor_id = Column(String(36), nullable=False)
 asset_type = Column(String(255), nullable=False)
 account_number = Column(LONGTEXT, nullable=False)
 meter_read = Column(String(255), nullable=True)
 meter_read_date = Column(String(255), nullable=True)
 created_at = Column(TIMESTAMP, nullable=True)
 updated_at = Column(TIMESTAMP, nullable=True)
 data_id = Column(String(255), nullable=True)