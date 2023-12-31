from ..schemas.notifierinformationschemas import NotifierRegistrationschema, DecedentRegistrationschema, CreateIdentificationSchemas, EditIdentificationSchema, RelationshipBaseSchema, CreateRelationshipSchemas, EditRelationshipSchema, FileUploadSchema, Status
from ..models.user_model import Users
from sqlalchemy.orm import Session
from ..models.requests_model import DecedentRequest, DecedentRequestDocument
from app.schemas.countriesapi import Countries,States,CountriesStates, Cities
from ..models.country_state_city_model import Country, State, City
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from ..models.identification_model import Identification
from ..models.relationship_model import Relationships
from fastapi import HTTPException, status, File, UploadFile, Form, Depends
from fastapi.responses import FileResponse
from sqlalchemy import update
from ..config.config import settings
import json, shutil,os, mimetypes
from pathlib import Path
import uuid
from ..service.hashing import Hasher
from uuid import uuid4
from sqlalchemyseed import load_entities_from_json
from sqlalchemyseed import Seeder


def create_new_notifier(notifier: NotifierRegistrationschema, user_id:str,db:Session):
    check_id=db.query(Users).filter(Users.id==user_id).first()
    if  not check_id:
        return 
     
    notifier = DecedentRequest (
    id=str(uuid4()),
    user_id= user_id,
    name= notifier.name,
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
    person_dealing_with_estate= notifier.person_dealing_with_estate,
    person_dealing_name= notifier.person_dealing_name,
    person_dealing_phone_number= notifier.person_dealing_phone_number,
    is_verify_identity= notifier.is_verify_identity,
    probate_applied= notifier.probate_applied,
    identification_id= notifier.identification_id,
    id_number=notifier.id_number
)
    db.add(notifier)
    db.commit()
    db.refresh(notifier)
    return notifier

def create_new_decedent(decedent: DecedentRegistrationschema, db:Session):
    check_id=db.query(DecedentRequest).filter(DecedentRequest.id==decedent.id).first()
    if check_id:
        decedent= update(DecedentRequest).where(DecedentRequest.id == decedent.id).values(ssn_number= Hasher.get_password_hash(decedent.ssn_number),
         decedent_first_name= decedent.decedent_first_name,
         decedent_last_name= decedent.decedent_last_name,
         present_address= decedent.present_address,
         present_address_two= decedent.present_address_two,
         previous_address= decedent.previous_address,
         previous_address_two= decedent.present_address_two,
         second_previous_address= decedent.second_previous_address,
         second_previous_address_two= decedent.second_previous_address,
         third_previous_address= decedent.third_previous_address,
         third_previous_address_two= decedent.third_previous_address_two,
         date_of_birth= decedent.date_of_birth,
         date_of_death= decedent.date_of_death,
         certificate_id= decedent.certificate_id,
         certificate_number= decedent.certificate_number)
    else:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f'ID does not exist')
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

async def get_countries_states_cities(db: Session):
  file_path = settings.COUNTRIES_API
  with open(file_path, 'r') as f:
     data = json.load(f)

  countries= []
  for country_data in data:
    country_obj = Country(id=country_data['id'], name=country_data['name'], countryCode=country_data['iso3'])
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
           city_obj = City(id=city_data['id'], name=city_data['name'], state_id=state_obj.id)
           existing_city= db.query(City).filter(City.id==city_data['id']).first()
           if not existing_city:
             db.add(city_obj)
             db.commit()
           cities.append(city_obj)
      
    countries.append(CountriesStates(country=Countries(id= country_obj.id, name= country_obj.name, countryCode= country_obj.countryCode), states=[States(id=state_obj.id, name=state_obj.name, country_id=country_obj.id, stateCode=state_obj.stateCode, cities= [Cities(id=city_obj.id,name=city_obj.name, state_id=state_obj.id) for city in cities])  for state in states]))
  return countries


# async def upload_and_download_file(
#  db: Session,
#  request_id: str = Form(...),
#  status: Status = Form(...),
#  files: List[UploadFile] = File(...)
# ):
#  uploaded_files = []

#  for file in files:
#    file_extension = mimetypes.guess_extension(file.content_type)
#    if file_extension not in ['.jpeg', '.jpg', '.pdf', '.png', '.doc', '.docx']:
#       raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs and image files are allowed.")

#    check_id = db.query(DecedentRequestDocument).filter(DecedentRequest.id == request_id).first()
#    if not check_id:
#       return f"The id doesn't match {request_id}"

#    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#    UPLOAD_DIR = os.path.join(BASE_DIR, settings.UPLOAD_DIR)
#    os.makedirs(UPLOAD_DIR, exist_ok=True)

#    DOWNLOAD_DIR = settings.DOWNLOAD_DIR
#    REQUEST_DIR = os.path.join(DOWNLOAD_DIR, request_id)

#    file_location = os.path.join(UPLOAD_DIR, file.filename)
#    os.makedirs(os.path.dirname(file_location), exist_ok=True)

#    with open(file_location, "wb") as buffer:
#       contents = await file.read()
#       buffer.write(contents)

#    download_path = os.path.join(REQUEST_DIR,file.filename)
#    os.makedirs(os.path.dirname(download_path), exist_ok=True)

#    with open(file_location, "rb") as source, open(download_path, "wb") as destination:
#       destination.write(source.read())

#    file_size = os.path.getsize(download_path)

#    # Create a new DecedentRequestDocument instance for each file
#    decedent_proof = DecedentRequestDocument(
#     id= str(uuid4()),
#     request_id=request_id,
#     document=download_path,
#     status= int(status.value),
#     size= file_size
#    )

#    # Save decedent_proof to the database
#    db.add(decedent_proof)
#    db.commit()
#    uploaded_files.append(file.filename)
#  return {"message": "Files uploaded successfully", "uploaded_files": uploaded_files}
# #  return FileResponse(path=download_path, media_type='application/octet-stream', filename=file.filename)
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
   check_id = db.query(DecedentRequestDocument).filter(DecedentRequest.id == request_id).first()
   if not check_id:
     return f"The id doesn't match {request_id}"

   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   UPLOAD_DIR = os.path.join(BASE_DIR, settings.UPLOAD_DIR)
   os.makedirs(UPLOAD_DIR, exist_ok=True)

   DOWNLOAD_DIR = settings.DOWNLOAD_DIR
   REQUEST_DIR = os.path.join(DOWNLOAD_DIR, request_id)

   file_location = os.path.join(UPLOAD_DIR, file.filename)
   os.makedirs(os.path.dirname(file_location), exist_ok=True)

   with open(file_location, "wb") as buffer:
     contents = await file.read()
     buffer.write(contents)

   download_path = os.path.join(REQUEST_DIR,file.filename)
   os.makedirs(os.path.dirname(download_path), exist_ok=True)

   with open(file_location, "rb") as source, open(download_path, "wb") as destination:
     destination.write(source.read())

   file_size = os.path.getsize(download_path)

 # Create a new DecedentRequestDocument instance for each file
   decedent_proof = DecedentRequestDocument(
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