import pycountry
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.database import get_db
from sqlalchemy.dialects.mysql import insert
import requests
from ..schemas.countriesapi import CountriesStates, CountryList, StatesList, CityList, CityDetailResponse, CityDetail
from ..repository.notifier import get_countries_states_cities, get_countries, get_states, get_cities, post_city_details



file_path = '/home/kishorerayan12/countries+states+cities.json'


router= APIRouter()

@router.get("/countries", response_model=list[CountriesStates])
async def get_all_countries_states_cities(db:Session= Depends(get_db)):
   get_countries= await get_countries_states_cities(db=db)
   return get_countries

@router.get("/get-countries", response_model=list[CountryList])
async def read_countries(db: Session = Depends(get_db)):
   return get_countries(db)

@router.get("/get-states", response_model=list[StatesList])
async def read_states(country_id:int, db: Session = Depends(get_db)):
   states= get_states(country_id=country_id, db=db)
   return states

@router.get("/get-cities", response_model=list[CityList])
async def read_cities(city_id: int, db: Session = Depends(get_db)):
   cities= get_cities(city_id=city_id, db=db)
   return cities

@router.post("/get-city_details", response_model=list[CityDetailResponse])
async def get_city_details(city_detail: CityDetail, db:Session= Depends(get_db)):
   cities= post_city_details(city_detail=city_detail, db=db)
   print("*********************",cities)
   return cities