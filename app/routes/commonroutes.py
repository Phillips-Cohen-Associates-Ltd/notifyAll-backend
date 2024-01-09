import pycountry
from fastapi import APIRouter, Depends, HTTPException,BackgroundTasks
from sqlalchemy.orm import Session
from ..config.database import get_db
from sqlalchemy.dialects.mysql import insert
import requests
from ..schemas.countriesapi import CountriesStates, CountryList, StatesList, CityList, CityDetailResponse, CityDetail, StateDetail,StateDetailResponse
from ..repository.notifier import load_countries_states_cities, get_countries, get_states, get_cities, post_city_details, post_state_details



file_path = '/home/kishorerayan12/countries+states+cities.json'


router= APIRouter()



@router.get("/countries")
async def get_all_countries_states_cities(background_tasks: BackgroundTasks):
   background_tasks.add_task(load_countries_states_cities)
   return {"message": "Loading countries, states, and cities..."}

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

@router.post("/get-state_details", response_model=list[StateDetailResponse])
async def get_state_details(state_detail:StateDetail,db:Session= Depends(get_db)):
   states= post_state_details(state_detail=state_detail, db=db)
   return states

@router.post("/get-city_details", response_model=list[CityDetailResponse])
async def get_city_details(city_detail:CityDetail,db:Session= Depends(get_db)):
    cities= post_city_details(city_detail==city_detail, db=db)
    return cities
   