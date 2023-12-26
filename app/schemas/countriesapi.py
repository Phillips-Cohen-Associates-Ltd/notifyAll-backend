from pydantic import BaseModel
from typing import List

class Countries(BaseModel):
  id: int
  name: str
  countryCode: str

class Cities(BaseModel):
   id: int
   name: str
   state_id: int

class States(BaseModel):
    id: int
    name: str
    country_id: int
    stateCode: str
    cities: List[Cities]



class CountriesStates(BaseModel):
  country: Countries
  states: list[States]
