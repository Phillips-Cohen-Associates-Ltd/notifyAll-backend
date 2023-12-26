from ..schemas.notifierinformationschemas import NotifierRegistrationschema, DecedentRegistrationschema, CreateIdentificationSchemas, EditIdentificationSchema, RelationshipBaseSchema, CreateRelationshipSchemas, EditRelationshipSchema
from sqlalchemy.orm import Session
from ..models.requests_model import DecedentRequest
from app.schemas.countriesapi import Countries,States,CountriesStates, Cities
from ..models.country_state_city_model import Country, State, City
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from ..models.identification_model import Identification
from ..models.relationship_model import Relationships
from fastapi import HTTPException, status
from sqlalchemy import update
import requests
from ..config.config import settings
import json


def create_new_notifier(notifier: NotifierRegistrationschema, db:Session):
    check_id=db.query(DecedentRequest).filter(DecedentRequest.user_id==notifier.user_id).first()
    if check_id:
        return
    notifier = DecedentRequest (
        user_id= notifier.user_id,
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
        decedent= update(DecedentRequest).where(DecedentRequest.id == decedent.id).values(ssn_number= decedent.ssn_number,
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

def get_countries_states_cities(db: Session):
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
