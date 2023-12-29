from datetime import date,datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import uuid4
import uuid
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from enum import Enum

class Relationship(str,Enum):
        son= "Son"
        daughter= "Daughter"
        spouse= "Spouse"
        attorney= "Attorney"
        executor= "Executor"
        executrix= "Executrix"
        funeral_Director= "Funeral Director"
        grand_Child= "Grand_child"
        next_of_kin= "Next_of_kin"
        Personal_representative= "Personal_representative"

class IDType(str,Enum):
        canadian_govt_id_cards= "Canadian Government ID Cards"
        canadian_permanent_resident_cards= "Canadian Permanent Resident Card"
        citizenship_cards= "Citizenship Cards"
        driver_license= "Driver License"
        passport= "passport"
        none= "None"

class Certificate_id(str,Enum):
       Death_certificate= "Death Certificate"
       Funeral_home_certificate= "Funeral Home Certificate"
       Medical_Report= "Medical Report"

class Status(int,Enum):
     success= 1
     Failed= 0


class NotifierRegistrationschema(BaseModel):
        # id: str
        # user_id: str
        name: str
        country: int
        address: str
        apartment: str
        country_code: str
        state: int
        city: int
        zipcode: str
        email: str
        phone_flag_code: str
        phone_number: str
        relationship: Relationship
        person_dealing_with_estate: bool
        person_dealing_name: Optional[str]
        person_dealing_phone_number: Optional[str]
        is_verify_identity: bool
        probate_applied: bool
        identification_id: Optional[IDType]
        id_number: Optional[str]
       
        class Config:
          from_attributes = True
          populate_by_name = True
          arbitrary_types_allowed = True
#    available_for_contact = Column(TINYINT(1), nullable=False)

class DecedentRegistrationschema(BaseModel):
       id: str
       ssn_number: str
       decedent_first_name: str
       decedent_last_name: str
       present_address: str        
       present_address_two: Optional[str]
       previous_address: Optional[str]
       previous_address_two: Optional[str]
       second_previous_address: Optional[str]
       second_previous_address_two: Optional[str]
       third_previous_address: Optional[str]
       third_previous_address_two: Optional[str]
       date_of_birth: Optional[date]
       date_of_death: Optional[date]
       certificate_id: Optional[Certificate_id]
       certificate_number: Optional[str]
       class Config:
          from_attributes = True
          populate_by_name = True
          arbitrary_types_allowed = True

# #    country_code = Column(String(5), nullable=False)
# #    level = Column(TINYINT, nullable=False)
# #    request_from = Column(Integer, nullable=False, server_default='1')
# #    excel_status = Column(Integer, nullable=False, server_default='0')
# #    request_status = Column(BigInteger, nullable=False, server_default='1')

class IdentificationBaseSchema(BaseModel):
    id: str | None = None
    name: str
    status: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


# def new_uuid() -> uuid.UUID:
#    # Generate a new UUID
#    val = uuid.uuid4()
#    # If the UUID starts with a zero, generate a new UUID
#    while val.hex[0] == '0':
#        val = uuid.uuid4()
#    return val

class CreateIdentificationSchemas(BaseModel):
#       id: uuid
      name: str
      status: int
      
      class Config:
        arbitrary_types_allowed = True

class EditIdentificationSchema(BaseModel):
    name: str
    id: str

# class DeleteIdentificationSchema(BaseModel):
#      id:str


class RelationshipBaseSchema(BaseModel):
    id: str | None = None
    name: str
    status: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class CreateRelationshipSchemas(BaseModel):
#       id: uuid
      name: str
      status: int
      
      class Config:
        arbitrary_types_allowed = True

class EditRelationshipSchema(BaseModel):
    name: str
    id: str

class FileUploadSchema(BaseModel):
    request_id: str  
    status: int




