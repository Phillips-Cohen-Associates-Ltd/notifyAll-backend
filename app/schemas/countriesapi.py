from pydantic import BaseModel
from typing import List, Optional

class Countries(BaseModel):
  id: int
  name: str
  countryCode: str
  iso2: str
  dial_code: str

class Cities(BaseModel):
   id: int
   name: str
   state_id: int
   country_id:int

class States(BaseModel):
    id: int
    name: str
    country_id: int
    stateCode: str
    cities: List[Cities]


class CountriesStates(BaseModel):
  country: Countries
  states: list[States]

class CountryList(BaseModel):
  id: int
  name: str
  countryCode: str
  iso2: Optional[str]
  dial_code: Optional[str]

class StatesList(BaseModel):
    id: int
    name: str
    country_id: int
    stateCode: str

class CityList(BaseModel):
   id: int
   name: str
   state_id: int
   country_id:int