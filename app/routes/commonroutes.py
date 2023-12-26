import pycountry
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.database import get_db
from sqlalchemy.dialects.mysql import insert
import requests
from ..schemas.countriesapi import CountriesStates
from ..repository.notifier import get_countries_states_cities



file_path = '/home/kishorerayan12/countries+states+cities.json'


router= APIRouter()

@router.get("/countries", response_model=list[CountriesStates])
def get_all_countries_states_cities(db:Session= Depends(get_db)):
   get_countries= get_countries_states_cities(db=db)
   return get_countries