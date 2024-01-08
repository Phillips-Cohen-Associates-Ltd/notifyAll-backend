from datetime import date,datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, validator, ValidationError
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

class Notifier_salutation(str,Enum):
     Mr= "Mr"
     Mrs="Mrs"
     Dr= "Dr"

class Decedent_salutation(str,Enum):
     Mr= "Mr"
     Mrs="Mrs"
     Dr= "Dr"

class NotifierRegistrationschema(BaseModel):
        # id: str
        # user_id: str
        Salutation: Notifier_salutation
        name: str
        middle_name: Optional[str]
        last_name:str
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
        is_spouse: bool
        spouse_sin: Optional[str]
        spouse_date_of_birth: Optional[date]
        spouse_first_name: Optional[str]
        spouse_middle_name: Optional[str]
        spouse_last_name: Optional[str]
        is_there_is_will: bool
        probate_applied: bool
     
        
        @validator('is_spouse')
        def check_is_spouse(cls, v):
          if v not in [False, True]:
            raise ValueError("is_spouse must be either False or True")
          return v

        @validator('spouse_sin', 'spouse_date_of_birth', 'spouse_first_name', 'spouse_last_name', pre=True, always=True)
        def check_spouse_details(cls, v,values):
          if 'is_spouse' in values and values['is_spouse'] == True:
               if v is None:
                 raise ValueError(f"Spouse details must be provided if is_spouse is True")
          return v
#    available_for_contact = Column(TINYINT(1), nullable=False)

class DecedentRegistrationschema(BaseModel):
       deceased_salutation: Decedent_salutation
       first_name_of_departed: str
       middle_name_of_departed: Optional[str]
       last_name_of_departed: str
       deceased_persons_phone_flag: str
       deceased_persons_phone_number: str
       deceased_persons_sex: str
       deceased_persons_marital_status:str
       deceased_persons_country: str
       deceased_persons_state: str
       deceased_persons_citizenship: str
       first_name_at_birth: Optional[str]
       last_name_at_birth : Optional[str]
       birth_city: int
       birth_state: int
       birth_country: int
       present_zipcode : str
       present_address: str        
       present_address_two: Optional[str]
       deceased_city1 : Optional[int]
       deceased_state1 : Optional[int]
       deceased_country: Optional[int]
       deceased_zipcode1 : Optional[str]
       deceased_address1: Optional[str]
       deceased_apt1: Optional[str]
       deceased_city2 : Optional[int]
       deceased_state2: Optional[int]
       deceased_address2: Optional[str]
       deceased_apt2: Optional[str]
#        second_previous_country: Optional[int]
       deceased_zipcode2 : Optional[str]
       deceased_city3 : Optional[int]
       deceased_state3:Optional[int]
#        third_previous_country: Optional[int]
       deceased_zipcode3 : Optional[str]    

       deceased_address3: Optional[str]
       deceased_apt3: Optional[str]
       date_of_birth: Optional[date]
       date_of_death: Optional[date]
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

class NotifierResponse(BaseModel):
        name: str
        middle_name: Optional[str]
        last_name:str
        country: int
        address: str
        apartment: str
        country_code: str
        state: int
        city: int
        zipcode: str
        email: str
        phone_flag_code: Optional[str]
        phone_number: str
        relationship: Relationship
        is_spouse: bool
        spouse_sin: Optional[str]
        spouse_date_of_birth: Optional[date]
        spouse_first_name: Optional[str]
        spouse_middle_name: Optional[str]
        spouse_last_name: Optional[str]
        is_there_is_will: bool
        probate_applied: bool
 
       
        class Config:
          from_attributes = True

class DecedentResponse(BaseModel):
       deceased_salutation: Decedent_salutation
       first_name_of_departed: str
       middle_name_of_departed: Optional[str]
       last_name_of_departed: str
       deceased_persons_phone_flag: str
       deceased_persons_phone_number: str
       deceased_persons_sex: str
       deceased_persons_marital_status:str
       deceased_persons_country: str
       deceased_persons_state: str
       deceased_persons_citizenship: str
       first_name_at_birth: Optional[str]
       last_name_at_birth : Optional[str]
       birth_city: int
       birth_state: int
       birth_country: int
       present_zipcode : str
       present_address: str        
       present_address_two: Optional[str]
       deceased_city1 : Optional[int]
       deceased_state1 : Optional[int]
       deceased_country: Optional[int]
       deceased_zipcode1 : Optional[str]
       deceased_address1: Optional[str]
       deceased_apt1: Optional[str]
       deceased_city2 : Optional[int]
       deceased_state2: Optional[int]
       deceased_address2: Optional[str]
       deceased_apt2: Optional[str]
#        second_previous_country: Optional[int]
       deceased_zipcode2 : Optional[str]
       deceased_city3 : Optional[int]
       deceased_state3:Optional[int]
#        third_previous_country: Optional[int]
       deceased_zipcode3 : Optional[str]    

       deceased_address3: Optional[str]
       deceased_apt3: Optional[str]
       date_of_birth: Optional[date]
       date_of_death: Optional[date]
       class Config:
          from_attributes = True

class UpdateNotifierSchema(BaseModel):
        name: str
        middle_name: Optional[str]
        last_name:str
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
        is_spouse: bool
        spouse_sin: Optional[str]
        spouse_date_of_birth: Optional[date]
        spouse_first_name: Optional[str]
        spouse_middle_name: Optional[str]
        spouse_last_name: Optional[str]
        is_there_is_will: bool
        probate_applied: bool

class UpdateDecedentSchema(BaseModel):
       deceased_salutation: Decedent_salutation
       first_name_of_departed: str
       middle_name_of_departed: Optional[str]
       last_name_of_departed: str
       deceased_persons_phone_flag: str
       deceased_persons_phone_number: str
       deceased_persons_sex: str
       deceased_persons_marital_status:str
       deceased_persons_country: str
       deceased_persons_state: str
       deceased_persons_citizenship: str
       first_name_at_birth: Optional[str]
       last_name_at_birth : Optional[str]
       birth_city: int
       birth_state: int
       birth_country: int
       present_zipcode : str
       present_address: str        
       present_address_two: Optional[str]
       deceased_city1 : Optional[int]
       deceased_state1 : Optional[int]
       deceased_country: Optional[int]
       deceased_zipcode1 : Optional[str]
       deceased_address1: Optional[str]
       deceased_apt1: Optional[str]
       deceased_city2 : Optional[int]
       deceased_state2: Optional[int]
       deceased_address2: Optional[str]
       deceased_apt2: Optional[str]
#        second_previous_country: Optional[int]
       deceased_zipcode2 : Optional[str]
       deceased_city3 : Optional[int]
       deceased_state3:Optional[int]
#        third_previous_country: Optional[int]
       deceased_zipcode3 : Optional[str]    

       deceased_address3: Optional[str]
       deceased_apt3: Optional[str]
       date_of_birth: Optional[date]
       date_of_death: Optional[date]