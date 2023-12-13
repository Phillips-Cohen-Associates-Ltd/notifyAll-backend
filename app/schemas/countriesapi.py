from pydantic import BaseModel

class Country(BaseModel):
 name: str
 isoCode: str
 countryCode: str
 

class State(BaseModel):
 name: str
 isoCode: str
 countryCode: str


class City(BaseModel):
 name: str
 countryCode: str
 stateCode: str
