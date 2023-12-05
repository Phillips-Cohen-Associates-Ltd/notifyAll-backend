from ..schemas import userschemas
from ..models import usermodel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from ..config.database import get_db
from ..repository.user import create_new_user, get_user_by_id, delete_user_by_id, update_user_by_id, check_and_update_user_password, authenticate_user, get_user_by_email, email_verification, forgot_password_by_email
from uuid import UUID 
from ..service.jwt import create_access_token
from ..service.sendmail import send_email_background
from ..service.hashing import Hasher
from jose import JWTError, jwt
from ..config.config import settings
from jinja2 import Environment, FileSystemLoader

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user-login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session= Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(email=username, db=db)
    if user is None:
        raise credentials_exception
    return user

# User Login
@router.post('/user-login')
def user_login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session= Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}

#get all users
# @router.get('/get-users')
# def get_users(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
#     skip = (page - 1) * limit

#     users = db.query(usermodel.Users).filter(
#         usermodel.Users.name.contains(search)).limit(limit).offset(skip).all()
#     return {'status': 'success', 'results': len(users), 'users': users}

#user registration
@router.post('/register-user', status_code=status.HTTP_201_CREATED)
def create_user(background_tasks: BackgroundTasks, user:userschemas.RegisterUsersSchema, db: Session = Depends(get_db)):
    new_user = create_new_user(user=user,db=db)
    if not new_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Email-id already exist')
    
    body_data = {
    "title": "Registration E-mail Verification",
    "name": f"{new_user.name}",
    "description": f"Your verification code is {new_user.verification_code}"
    }
    # body_json = json.dumps(body_data)
    # Load the template
    env = Environment(loader=FileSystemLoader('/home/kishorerayan12/notifyAll-backend/app/templates'))
    template = env.get_template('emailVerification.html')

    # Render the template with the dictionary
    html_output = template.render(body_data)

    send_email_background(background_tasks, f'Registration E-mail Verification', f'{new_user.email}', html_output)
    return {"status": "success", "message": "User registered successfully"}

@router.post('/verify-email')
def verify_email(payload: userschemas.UserEmailVerificationSchema, db: Session = Depends(get_db)):
    verification = email_verification(payload = payload, db=db)
    if not verification:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Your e-mail id can't be verified")
         
    return{"status": "sucsess", "message":"E-mail id verified successfully"}

#Get User detail by ID   
@router.get('/get-user', response_model=userschemas.ShowUsersResponse)
def get_user(db: Session = Depends(get_db), currentUser:usermodel.Users=Depends(get_current_user)):
    # try:
    #     user_uuid = UUID(userId)
    # except ValueError:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f'No user with this id: {userId} found')
    user = get_user_by_id(userId = currentUser.id, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No user with this id: {currentUser.id} found")
    # return {"status": "success", "users": user}
    return user


#update user by ID
@router.patch('/update-user')
def update_user(payload: userschemas.UpdateUserSchema, db: Session = Depends(get_db), currentUser:usermodel.Users=Depends(get_current_user)):
    # try:
    #     user_uuid = UUID(userId)
    # except ValueError:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f'No user with this id: {userId} found')
        
    user = update_user_by_id(userId = currentUser.id, payload=payload, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No user found or E-mail ID already taken')
    
    return {"status": "success", "message": "User details updated successfully"}

#Changes User's password
@router.patch('/change-password')
def change_password(payload: userschemas.UpdateUserPasswordSchema, db:Session = Depends(get_db), currentUser: usermodel.Users=Depends(get_current_user)):
        
    check_password = check_and_update_user_password(currentUser=currentUser, payload=payload , db=db)
    if not check_password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'User ID or old password mismatch')
        
    return {"status": "success", "message": "User password updated successfully "}

#Get User detail by ID   
@router.get('/get-user', response_model=userschemas.ShowUsersResponse)
def get_user(db: Session = Depends(get_db), currentUser:usermodel.Users=Depends(get_current_user)):
    # try:
    #     user_uuid = UUID(userId)
    # except ValueError:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f'No user with this id: {userId} found')
    user = get_user_by_id(userId = currentUser.id, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No user with this id: {userId} found")
    # return {"status": "success", "users": user}
    return user


#Delete user by ID
@router.delete('/delete-user/{userId}')
def delete_user(userId: str, db: Session = Depends(get_db), currentUser:usermodel.Users=Depends(get_current_user)):
    user = delete_user_by_id(userId = userId, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No user with this id: {userId} found')
    
    return {"msg":f"Successfully deleted user with id {userId}"}
    # return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post('/forgot_password')
@staticmethod
def forgot_password(background_tasks: BackgroundTasks,user: userschemas.ForgotPasswordSchema, db: Session= Depends(get_db)):
    update_password= forgot_password_by_email(user=user, db=db)
    if not update_password:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No user with this email found')
    body_data = {
    "title": "Registration password Verification",
    "name": f"{update_password.name}",
    "description": f"Your verification code is {update_password.verification_code}"
    }
    # body_json = json.dumps(body_data)
    # Load the template
    env = Environment(loader=FileSystemLoader('/home/kishorerayan12/notifyAll-backend/app/templates'))
    template = env.get_template('passwordverification.html')

    html_output = template.render(body_data)

    send_email_background(background_tasks, f'Forgot Password Verification', f'{update_password.email}', html_output)
    return {"status": "success", "message": "forgot password code sent successfully"}



@router.post('/reset_password')
def reset_password(user: userschemas.ResetPasswordSchema, db: Session = Depends(get_db)):
    user_to_reset = db.query(usermodel.Users).filter(usermodel.Users.verification_code == user.verification_code and usermodel.Users.email== user.email).first()
    if not user_to_reset:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Invalid verification code')
    
    user_to_reset.password = Hasher.get_password_hash(user.new_password)
    db.add(user_to_reset)
    db.commit()

    return {"status": "success", "message": "password reset successfully"}



































































































