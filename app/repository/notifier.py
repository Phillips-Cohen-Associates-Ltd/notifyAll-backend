from ..schemas.notifierinformationschemas import NotifierRegistrationschema, DecedentRegistrationschema, CreateIdentificationSchemas, EditIdentificationSchema, RelationshipBaseSchema, CreateRelationshipSchemas, EditRelationshipSchema, FileUploadSchema, Status, UpdateNotifierSchema, UpdateDecedentSchema
from ..models.user_model import Users
from sqlalchemy.orm import Session
from ..models.requests_model import DecedentRequestsDraft, DecedentRequestDocumentDraft
from app.schemas.countriesapi import Countries,States,CountriesStates, Cities, CityDetail, StateDetail
from ..models.country_state_city_model import Country, State, City
from typing import List, Union
from pydantic import BaseModel, validator, ValidationError
from sqlalchemy.exc import SQLAlchemyError
from ..models.identification_model import Identification
from ..models.relationship_model import Relationships
from fastapi import HTTPException, status, File, UploadFile, Form, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import update
from ..config.config import settings
import json, shutil,os, mimetypes
from pathlib import Path
import uuid
from ..config.database import SessionLocal
from ..service.hashing import Hasher
from uuid import uuid4
from sqlalchemyseed import load_entities_from_json
from sqlalchemyseed import Seeder
from datetime import datetime, date



def create_new_notifier(notifier: NotifierRegistrationschema, user_id:str, db:Session):
 check_id=db.query(Users).filter(Users.id==user_id).first()
 if not check_id:
     return JSONResponse({
           "status": False,
           "message": {"error": "User ID does not exist"},
           "statusCode": 403
       })
 

 try:
     notifier = DecedentRequestsDraft (
      id=str(uuid4()),
      notifier_salutation= notifier.Salutation,
      user_id= user_id,
      name= notifier.name,
      middle_name= notifier.middle_name,
      last_name= notifier.last_name,
      country= notifier.country,
      address= notifier.address,
      address_two= notifier.apartment,
      state= notifier.state,
      city= notifier.city,
      country_code= notifier.country_code,
      zipcode=notifier.zipcode,
      email=notifier.email,
      phone_number= notifier.phone_number,
      relationship= notifier.relationship,
      is_spouse= notifier.is_spouse,
      spouse_sin= notifier.spouse_sin,
      # spouse_date_of_birth=notifier.spouse_date_of_birth,
      spouse_first_name=notifier.spouse_first_name,
      spouse_middle_name=notifier.spouse_middle_name,
      spouse_last_name=notifier.spouse_last_name,
      probate_applied= notifier.probate_applied,
      is_there_is_will= notifier.is_there_is_will
  )
 except ValidationError as e:
   errors = e.json()
   error_messages = {}
   for error in errors['detail']:
       field = error['loc'][0]
       error_messages[field] = f"{field} is required"
   raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=error_messages)     
 db.add(notifier)
 db.commit()
 db.refresh(notifier)

 data = notifier.__dict__

 data.pop('_sa_instance_state', None)


 return JSONResponse({
    "status": True,
    "message": "Notifier account created successfully",
    "statusCode": 201,
    "data": data
 })

def create_new_decedent( id:str,decedent: DecedentRegistrationschema,db:Session):
    check_id=db.query(DecedentRequestsDraft).filter(DecedentRequestsDraft.id==id).first()
    if check_id:
        decedent= update(DecedentRequestsDraft).where(DecedentRequestsDraft.id == id).values(
       deceased_salutation=decedent.deceased_salutation,
       first_name_of_departed=decedent.first_name_of_departed,
       middle_name_of_departed=decedent.middle_name_of_departed,
       last_name_of_departed=decedent.last_name_of_departed,
       deceased_persons_phone_flag=decedent.deceased_persons_phone_flag,
       deceased_persons_phone_number=decedent.deceased_persons_phone_number,
       deceased_persons_sex=decedent.deceased_persons_sex,
       deceased_persons_marital_status=decedent.deceased_persons_marital_status,
       deceased_persons_country=decedent.deceased_persons_country,
       deceased_persons_state=decedent.deceased_persons_state,
       deceased_persons_citizenship=decedent.deceased_persons_citizenship,
       decedent_first_name=decedent.first_name_at_birth,
       decedent_last_name=decedent.last_name_at_birth,
      present_city=decedent.birth_city,
      present_state=decedent.birth_state,
      present_country=decedent.birth_country,
      present_zipcode=decedent.present_zipcode,
      present_address=decedent.present_address,
      present_address_two=decedent.present_address_two,
      previous_city=decedent.deceased_city1,
      previous_state=decedent.deceased_state1,
      previous_country=decedent.deceased_country,
      previous_zipcode=decedent.deceased_zipcode1,
      previous_address=decedent.deceased_address1,
      previous_address_two=decedent.deceased_apt1,
      second_previous_city=decedent.deceased_city2,
      second_previous_state=decedent.deceased_state2,
      second_previous_zipcode=decedent.deceased_zipcode2,
      third_previous_city=decedent.deceased_city3,
      third_previous_state=decedent.deceased_state3,
      third_previous_zipcode=decedent.deceased_zipcode3,
      second_previous_address=decedent.deceased_address2,
      second_previous_address_two=decedent.deceased_apt2,
      third_previous_address=decedent.deceased_address3,
      third_previous_address_two=decedent.deceased_apt3,
      date_of_birth=decedent.date_of_birth,
      date_of_death=decedent.date_of_death
      )
    else:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f'ID does not exist')
    db.execute(decedent)
    db.commit()
    return True

def get_notifier_by_id(user_id:str, id:str, db:Session):
  notifier= db.query(DecedentRequestsDraft).filter(DecedentRequestsDraft.user_id==user_id, 
                                                   DecedentRequestsDraft.id==id).first()
  return notifier

def get_decedent_by_id(user_id:str,id:str, db:Session):
   decedent= db.query(DecedentRequestsDraft).filter(DecedentRequestsDraft.user_id==user_id,DecedentRequestsDraft.id==id).first()
   return decedent

def update_notifier_by_id(notifier: UpdateNotifierSchema,user_id:str,id:str, db:Session):
  verify_id= db.query(DecedentRequestsDraft).filter(DecedentRequestsDraft.user_id==user_id , DecedentRequestsDraft.id==id).first()
  if not verify_id:
       return
  notifier= update(DecedentRequestsDraft).where(DecedentRequestsDraft.user_id == user_id).values(
      name= notifier.name,
      middle_name= notifier.middle_name,
      last_name= notifier.last_name,
      country= notifier.country,
      address= notifier.address,
      apartment= notifier.apartment,
      state= notifier.state,
      city= notifier.city,
      country_code= notifier.country_code,
      zipcode=notifier.zipcode,
      email=notifier.email,
      phone_number= notifier.phone_number,
      relationship= notifier.relationship,
      is_spouse= notifier.is_spouse,
      spouse_sin= notifier.spouse_sin,
      spouse_date_of_birth=notifier.spouse_date_of_birth,
      spouse_first_name=notifier.spouse_first_name,
      spouse_middle_name=notifier.spouse_middle_name,
      spouse_last_name=notifier.spouse_last_name,
      probate_applied= notifier.probate_applied,
      is_there_is_will= notifier.is_there_is_will
  )
  db.execute(notifier)
  db.commit()
  return True

def update_decedent_by_id(id:str,decedent: UpdateDecedentSchema,user_id:str, db:Session):
    verify_id= db.query(DecedentRequestsDraft).filter(DecedentRequestsDraft.user_id==user_id, DecedentRequestsDraft.id==id).first()
    if not verify_id:
       return
    decedent= update(DecedentRequestsDraft).where(DecedentRequestsDraft.user_id == user_id).values( deceased_salutation=decedent.deceased_salutation,
      eceased_salutation=decedent.deceased_salutation,
       first_name_of_departed=decedent.first_name_of_departed,
       middle_name_of_departed=decedent.middle_name_of_departed,
       last_name_of_departed=decedent.last_name_of_departed,
       deceased_persons_phone_flag=decedent.deceased_persons_phone_flag,
       deceased_persons_phone_number=decedent.deceased_persons_phone_number,
       deceased_persons_sex=decedent.deceased_persons_sex,
       deceased_persons_marital_status=decedent.deceased_persons_marital_status,
       deceased_persons_country=decedent.deceased_persons_country,
       deceased_persons_state=decedent.deceased_persons_state,
       deceased_persons_citizenship=decedent.deceased_persons_citizenship,
       decedent_first_name=decedent.first_name_at_birth,
       decedent_last_name=decedent.last_name_at_birth,
      present_city=decedent.birth_city,
      present_state=decedent.birth_state,
      present_country=decedent.birth_country,
      present_zipcode=decedent.present_zipcode,
      present_address=decedent.present_address,
      present_address_two=decedent.present_address_two,
      previous_city=decedent.deceased_city1,
      previous_state=decedent.deceased_state1,
      previous_country=decedent.deceased_country,
      previous_zipcode=decedent.deceased_zipcode1,
      previous_address=decedent.deceased_address1,
      previous_address_two=decedent.deceased_apt1,
      second_previous_city=decedent.deceased_city2,
      second_previous_state=decedent.deceased_state2,
      second_previous_zipcode=decedent.deceased_zipcode2,
      third_previous_city=decedent.deceased_city3,
      third_previous_state=decedent.deceased_state3,
      third_previous_zipcode=decedent.deceased_zipcode3,
      second_previous_address=decedent.deceased_address2,
      second_previous_address_two=decedent.deceased_apt2,
      third_previous_address=decedent.deceased_address3,
      third_previous_address_two=decedent.deceased_apt3,
      date_of_birth=decedent.date_of_birth,
      date_of_death=decedent.date_of_death)
    
    db.execute(decedent)
    db.commit()
    return True


def create_new_identification(identification: CreateIdentificationSchemas, db:Session):
    identification= Identification(
        name= identification.name,
        status= identification.status
    )
    db.add(identification)
    db.commit()
    db.refresh(identification)
    return identification

def edit_identification_by_id(editidentification: EditIdentificationSchema, db: Session):
    verify_id= db.query(Identification).filter(Identification.id==editidentification.id).first()
    if not verify_id:
        return
    editidentification= update(Identification).where(Identification.id == editidentification.id).values(name= editidentification.name)
    db.execute(editidentification)
    db.commit()
    return True

def delete_identification_by_id(id:str, db:Session):
    delete_by_id= db.query(Identification).filter(Identification.id==id)
    if not delete_by_id:
        return
    delete_by_id.delete(synchronize_session=False)
    db.commit()
    return 1


def create_new_relationship(relationship:CreateRelationshipSchemas , db:Session):
    relationship= Relationships(
        name= relationship.name,
        status= relationship.status
    )
    db.add(relationship)
    db.commit()
    db.refresh(relationship)
    return relationship


def edit_relationship_by_id(editrelationship: EditRelationshipSchema, db: Session):
    verify_id= db.query(Relationships).filter(Relationships.id==editrelationship.id).first()
    if not verify_id:
        return
    editrelationship= update(Relationships).where(Relationships.id == editrelationship.id).values(name= editrelationship.name)
    db.execute(editrelationship)
    db.commit()
    return True


def delete_relationship_by_id(id:str, db:Session):
    delete_by_id= db.query(Relationships).filter(Relationships.id==id)
    if not delete_by_id:
        return
    delete_by_id.delete(synchronize_session=False)
    db.commit()
    return 1

async def load_countries_states_cities():
  file_path = settings.COUNTRIES_API
  db=SessionLocal()
  try:
     with open(file_path, 'r') as f:
       data = json.load(f)

     countries= []
     for country_data in data:
        country_obj = Country(id=country_data['id'], name=country_data['name'], countryCode=country_data['iso3'], iso2= country_data['iso2'], dial_code=country_data['phone_code'])
        existing_country = db.query(Country).filter(Country.id == country_data['id']).first()
        if not existing_country:
          db.add(country_obj)
          db.commit()
        states=[]
        for state_data in country_data['states']: #loop through each state in the country
           state_obj = State(id=state_data['id'], name=state_data['name'], stateCode=state_data['state_code'], country_id=country_obj.id)
           existing_state = db.query(State).filter(State.id == state_data['id']).first()
           if not existing_state:
              db.add(state_obj)
              db.commit()
           states.append(state_obj)
           cities=[]
           for city_data in state_data['cities']: # Loop through each city in the state
              city_obj = City(id=city_data['id'], name=city_data['name'], state_id=state_obj.id, country_id= country_obj.id)
              existing_city= db.query(City).filter(City.id==city_data['id']).first()
              if not existing_city:
                db.add(city_obj)
                db.commit()
              cities.append(city_obj)
      
        countries.append(CountriesStates(country=Countries(id= country_obj.id, name= country_obj.name, countryCode= country_obj.countryCode, iso2= country_obj.iso2, dial_code=country_obj.dial_code), states=[States(id=state_obj.id, name=state_obj.name, country_id=country_obj.id, stateCode=state_obj.stateCode, cities= [Cities(id=city_obj.id,name=city_obj.name, state_id=state_obj.id, country_id=country_obj.id) for city in cities])  for state in states]))
     return countries
  finally:
     db.close()

def get_countries(db:Session):
   countries=db.query(Country).all()
   return countries

def get_states(country_id:int, db:Session):
   states= db.query(State).filter(State.country_id==country_id).all()
   if not states: 
      return f"The id doesn't match {country_id}"
 
   return states

def get_cities( city_id: int,db:Session):
   cities= db.query(City).filter(City.id==city_id).all()
   if not cities: 
      return []
   return cities


def post_state_details(db:Session,state_detail= StateDetail):
   states= db.query(State).filter(State.country_id== state_detail.country_id, State.name==state_detail.name).all()
   if not states:
         return []
   return states

def post_city_details(db:Session,city_detail= CityDetail):
   cities= db.query(City).filter(City.country_id== city_detail.country_id, City.state_id==city_detail.state_id, City.name==city_detail.city).all()
   print("*********************", cities)
   if not cities:
         return []
   return cities


async def upload_and_download_file(
 db: Session,
 request_id: str = Form(...),
 status: Status = Form(...),
 files: List[UploadFile] = File(...)
):
 uploaded_files = []
 valid_files = True # Flag to track if all files are valid

 for file in files:
   file_extension = mimetypes.guess_extension(file.content_type)
   if file_extension not in ['.jpeg', '.jpg', '.pdf', '.png', '.doc', '.docx']:
      valid_files = False # Set flag to False if a file fails the condition
      break
   check_id = db.query(DecedentRequestsDraft).filter(DecedentRequestsDraft.id ==request_id).first()
   print("***************",check_id)
   if not check_id:
     return f"The id doesn't match {request_id}"

   DOWNLOAD_DIR = settings.DOWNLOAD_DIR
   REQUEST_DIR = os.path.join(DOWNLOAD_DIR, request_id)

   download_path = os.path.join(REQUEST_DIR,file.filename)
   os.makedirs(os.path.dirname(download_path), exist_ok=True)

   with open(download_path, "wb") as destination:
       contents = await file.read()
       destination.write(contents)

   file_size = os.path.getsize(download_path)

 # Create a new DecedentRequestDocument instance for each file
   decedent_proof = DecedentRequestDocumentDraft(
 id= str(uuid4()),
 request_id=request_id,
 document=download_path,
 status= int(status.value),
 size= file_size
 )

 # Add decedent_proof to the session but don't commit yet
   db.add(decedent_proof)

   uploaded_files.append(file.filename)

 # If any file failed the condition, rollback the session and return an error message
 if not valid_files:
   db.rollback()
   return {"error": "Some files have invalid extensions."}

 # Otherwise, commit the changes to the database
 db.commit()

 return {"message": "Files uploaded successfully", "uploaded_files": uploaded_files}