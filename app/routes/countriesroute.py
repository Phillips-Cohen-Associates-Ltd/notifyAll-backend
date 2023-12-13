import pycountry
from app.schemas.countriesapi import Country, State, City
from fastapi import APIRouter
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter



router= APIRouter()

@router.get("/countries", response_model=list[Country])
def get_countries():
 countries = [Country(name=country.name, isoCode=country.alpha_2, countryCode=country.alpha_3) for country in pycountry.countries]
 return countries

@router.get("/countries/{country_code}/states", response_model=list[State])
def get_states(country_code: str):
 country = pycountry.countries.get(alpha_2=country_code)
 if country is None:
  return []
 subdivisions = pycountry.subdivisions.get(country_code=country_code)
 if subdivisions is None:
  return []
 states = [State(name=state.name, isoCode=state.code, countryCode=country.alpha_3) for state in subdivisions]
 return states


def get_city_details(city_name):
   geolocator = Nominatim(user_agent="notifyAll")
   location = geolocator.geocode(city_name)
   geolocator = RateLimiter(geolocator,min_delay_seconds=1)
   return location.address

@router.get("/countries/{country_code}/states/{state_code}/cities", response_model=list[City])
def get_cities(country_code: str, state_code: str):
   country = pycountry.countries.get(alpha_2=country_code)
   if country is None:
       return []
   state = pycountry.subdivisions.get(code=state_code)
   if state is None:
       return []
   cities = [City(name=get_city_details(city), countryCode=country.alpha_3, stateCode=state.code) for city in state.name]
   print(state.name)
   return cities

