from fastapi import APIRouter,status, Depends, HTTPException, UploadFile, File,Form
from fastapi.responses import FileResponse
from ..schemas.notifierinformationschemas import NotifierRegistrationschema, DecedentRegistrationschema, IdentificationBaseSchema, CreateIdentificationSchemas, EditIdentificationSchema, RelationshipBaseSchema, CreateRelationshipSchemas, EditRelationshipSchema, FileUploadSchema,Status
from sqlalchemy.orm import Session
from ..models.requests_model import DecedentRequestDocument, DecedentRequest
from ..models.user_model import Users
from ..repository.notifier import create_new_notifier, create_new_decedent, create_new_identification, edit_identification_by_id, delete_identification_by_id, create_new_relationship, edit_relationship_by_id, delete_relationship_by_id, upload_and_download_file
from ..config.database import get_db
import json, os, shutil, mimetypes
from typing import List
import time 
timestr= time.strftime("%Y%m%d-%H%M%S")
router= APIRouter()

@router.post('/notifier-register', status_code=status.HTTP_201_CREATED)
def create_notifier(notifier:NotifierRegistrationschema, user_id:str, db: Session = Depends(get_db)):
    new_user = create_new_notifier(notifier=notifier,user_id=user_id,db=db)
    if not new_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'ID doesnt exists')
    return "notifier account created successfully"

@router.post('/decedent-register', status_code=status.HTTP_201_CREATED)
def create_decedent(decedent:DecedentRegistrationschema, db: Session = Depends(get_db)):
    new_user = create_new_decedent(decedent= decedent,db=db)
    if not new_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'ID already exists')
    return "decedent account created successfully"

@router.post('/create-identification', status_code=status.HTTP_201_CREATED)
def create_identification(identification:CreateIdentificationSchemas, db: Session= Depends(get_db)):
    new_identification= create_new_identification(identification=identification, db=db)
    if not new_identification:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'ID already exists')
    return "Identification Id created successfully"

@router.post('/edit-identification', status_code=status.HTTP_201_CREATED)
def edit_identification(editidentification:EditIdentificationSchema, db:Session= Depends(get_db)):
    updated_identification_name= edit_identification_by_id(editidentification=editidentification, db=db)
    print(updated_identification_name)
    if not updated_identification_name:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'ID doesnt exists')
    return "Identification Id updated successfully"



@router.post('/delete-identification', status_code=status.HTTP_201_CREATED)
def delete_identification(id:str, db:Session= Depends(get_db)):
    deleted_id= delete_identification_by_id(id=id, db=db)
    if not deleted_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'ID already exists')
    return "Identification Id deleted successfully"


@router.post('/create-relationship', status_code=status.HTTP_201_CREATED)
def create_relationship(relationship: CreateRelationshipSchemas, db: Session= Depends(get_db)):
    new_relationship= create_new_relationship(relationship=relationship, db=db)
    if not new_relationship:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'ID already exists')
    return "Relationship created successfully"


# @router.post('/edit-relationship', status_code=status.HTTP_201_CREATED)
# def edit_relationship(editrelationship:EditRelationshipSchema, db:Session= Depends(get_db)):
#     updated_relationship= edit_relationship_by_id(editrelationship=editrelationship, db=db)
#     if not updated_relationship:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                             detail=f'ID already exists')
#     return "Identification Id updated successfully"


@router.post('/edit-relationship', status_code=status.HTTP_201_CREATED)
def edit_relationship(editrelationship:EditRelationshipSchema, db:Session= Depends(get_db)):
    updated_relationship_name= edit_relationship_by_id(editrelationship=editrelationship, db=db)
    print(updated_relationship_name)
    if not updated_relationship_name:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'ID doesnt exists')
    return "relationship Id updated successfully"



@router.post('/delete-relationship', status_code=status.HTTP_201_CREATED)
def delete_relationship(id:str, db:Session= Depends(get_db)):
    deleted_id= delete_relationship_by_id(id=id, db=db)
    if not deleted_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'ID already exists')
    return "Identification Id deleted successfully"

@router.post('/uploadanddownloadfile')
async def downloadfiles(request_id: str= Form(), status: Status= Form(...),
   db: Session= Depends(get_db),
   files: List[UploadFile] = File(...)):
    download_file= await upload_and_download_file(request_id=request_id,status=status,db=db,files=files)
    return download_file
