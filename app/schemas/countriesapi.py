from pydantic import BaseModel

class Countries(BaseModel):
 name: str
 isoCode: str
 countryCode: str
 

class States(BaseModel):
 name: str
 isoCode: str
 countryCode: str


class Cities(BaseModel):
 name: str
 countryCode: str
 stateCode: str
