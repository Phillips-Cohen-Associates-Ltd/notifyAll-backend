from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import Depends
from ..schemas.userschemas import UsersBaseSchema, RegisterUsersSchema, UpdateUserSchema, UpdateUserPasswordSchema, UserEmailVerificationSchema, ForgotPasswordSchema, ResetPasswordSchema
from ..models.user_model import Users
from ..config.database import get_db
from ..service.hashing import Hasher
from..service.utils import Utils
import pycountry


def create_new_user(user:RegisterUsersSchema,db:Session):
    check_email = db.query(Users).filter(Users.email == user.email).first()
    if check_email:
        return
    
    user = Users(
        name = user.name,
        email = user.email,
        password=Hasher.get_password_hash(user.password),
        is_approved=False,
        is_email_verified=False,
        verification_code=Utils.generate_random_code()
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user_by_id(userId: str, payload: UpdateUserSchema, db: Session):
    try:
        check_email_availability = db.query(Users).filter(and_(Users.email == payload.email, Users.id != userId)).first()
        if check_email_availability:
            return
        
        user_query = db.query(Users).filter(Users.id == userId)
        db_user = user_query.first()
        
        if not db_user:
            return

        for attr, value in payload.dict(exclude_unset=True).items():
            if attr == 'password':
                # Encrypt the password
                db_user.password = Hasher.get_password_hash(value)
            else:
                setattr(db_user, attr, value)
                
        # update_data = payload.dict(exclude_unset=True)
        # user_query.filter(Users.id == userId).update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(db_user)
        return db_user
    except ValueError as ve:
        return ve


def get_user_by_id(userId: str, db:Session):
    user = db.query(Users).filter(Users.id == userId).first()
    return user

def get_user_by_email(email: str, db:Session):
    user = db.query(Users).filter(Users.email == email).first()
    return user

def check_and_update_user_password(currentUser:UsersBaseSchema, payload: UpdateUserPasswordSchema, db:Session):
    verify_password = Hasher.verify_password(payload.old_password, currentUser.password)
    if not verify_password:
        return
    new_password = Hasher.get_password_hash(payload.new_password)
    db.query(Users).filter(Users.id == currentUser.id).update({"password":new_password})
    db.commit()
    return 1


def delete_user_by_id(userId: str, db:Session):
    user = db.query(Users).filter(Users.id == userId)
    user_data = user.first()
    if not user_data:
        return
    
    user.delete(synchronize_session=False)
    db.commit()
    return 1

def authenticate_user(email: str, password: str,db: Session):
    user = get_user_by_email(email=email,db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user

def email_verification(payload: UserEmailVerificationSchema, db: Session):
    user = db.query(Users).filter(and_(Users.email == payload.email, Users.verification_code == payload.verification_code)).first()
    if not user:
        return False
    
    db.query(Users).filter(Users.id == user.id).update({"is_approved":True, "is_email_verified":True})
    db.commit()
    return 1

def forgot_password_by_email(user: ForgotPasswordSchema, db:Session):
   identify_user = db.query(Users).filter(Users.email==user.email).first()
   if not identify_user:
       return 
   
   identify_user.verification_code=Utils.generate_random_code()
   db.commit()
   db.refresh(identify_user)
   return identify_user
