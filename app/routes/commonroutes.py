import pycountry
from app.schemas.countriesapi import Countries, States, Cities
from fastapi import APIRouter, Depends, HTTPException
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import geopandas as gpd
from geopandas.tools import geocode
from sqlalchemy.orm import Session
from ..models.countries_state_citymodel import Country, State, City
from ..config.database import get_db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.mysql import insert






router= APIRouter()

@router.get("/countries", response_model=list[Countries])
def get_countries(db: Session = Depends(get_db)):
   countries = [Country(name=country.name, isoCode=country.alpha_2, countryCode=country.alpha_3) for country in pycountry.countries]
   existing_countries = db.query(Country).all()
   existing_isoCodes = {country.isoCode for country in existing_countries}

   new_countries = [country for country in countries if country.isoCode not in existing_isoCodes]

   db.bulk_save_objects(new_countries)
   db.commit()

   return countries

@router.get("/countries/{country_code}/states", response_model=list[States])
def get_states(country_code: str, db: Session = Depends(get_db)):
  country = pycountry.countries.get(alpha_2=country_code)
  subdivisions = pycountry.subdivisions.get(country_code=country_code)

  # Get all existing states from the database
  existing_states = db.query(State).all()
  existing_names = {state.name for state in existing_states}

  states = []
  for state in subdivisions:
      # Check if the state already exists in the database
      if state.name not in existing_names:
          new_state = State(name=state.name, isoCode=state.code, countryCode=country.alpha_3)
          db.add(new_state)
          states.append(new_state)
  db.commit()
  states = [State(name=state.name, isoCode=state.code, countryCode=country.alpha_3) for state in subdivisions]

  return states


# def get_city_details(city_name):
#     geolocator = Nominatim(user_agent="notifyAll")
#     location = geolocator.geocode(city_name)
#     geolocator = RateLimiter(geolocator,min_delay_seconds=5)
#     return location.address

# @router.get("/countries/{country_code}/states/{state_code}/cities", response_model=list[Cities])
# @router.get("/countries/{country_code}/states/{state_code}/cities", response_model=list[Cities])
# def get_cities(country_code: str, state_code: str, db: Session = Depends(get_db)):
#  country = pycountry.countries.get(alpha_2=country_code)
#  if country is None:
#    return []
#  state = pycountry.subdivisions.get(code=state_code)
#  if state is None:
#    return []

#  # Get all existing cities from the database
#  existing_cities = db.query(City).all()
#  existing_names = {city.name for city in existing_cities}

#  cities = []
#  for city in state.name:
#    # Check if the city already exists in the database
#    if city not in existing_names:
#        city_details = get_city_details(city)
#        if city_details is not None:
#            new_city = City(name=city_details, countryCode=country.alpha_3, stateCode=state.code)
#            db.add(new_city)
#            cities.append(new_city)
#  db.commit()
#  return cities


def get_city_details(city_name):
   gdf = geocode(city_name, provider="nominatim", user_agent="notifyAll")
   name= gdf.iloc[0].address
   return str(name)

@router.get("/countries/{country_code}/states/{state_code}/cities", response_model=list[Cities])
def get_cities(country_code: str, state_code: str, db: Session = Depends(get_db)):
 country = pycountry.countries.get(alpha_2=country_code)
 if country is None:
  return []
 state = pycountry.subdivisions.get(code=state_code)
 if state is None:
  return []

 # Get all existing cities from the database
 existing_cities = db.query(City).all()
 existing_names = {city.name for city in existing_cities}

 cities = []
 for city in state.name:
  # Check if the city already exists in the database
  if city not in existing_names:
      city_details = get_city_details(city)
      if city_details is not None:
          new_city = City(name=city_details, countryCode=country.alpha_3, stateCode=state.code)
          db.add(new_city)
          cities.append(new_city)
 db.commit()
 cities = City(name=city_details, countryCode=country.alpha_3, stateCode=state.code)
 print(cities)
 return cities