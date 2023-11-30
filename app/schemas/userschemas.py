from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, Field, UUID4


class UsersBaseSchema(BaseModel):
    id: str | None = None
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    is_approved: bool = False
    is_email_verified: bool = False
    verification_code: str | None = None
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
        
        
class RegisterUsersSchema(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    
        
class UpdateUserSchema(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class UpdateUserPasswordSchema(BaseModel):
    old_password: str = Field(..., min_length=8)
    new_password: str = Field(..., min_length=8)
    
    
class UserEmailVerificationSchema(BaseModel):
    verification_code: str = Field(..., min_length=6)
    email: EmailStr
    
class ShowUsersResponse(BaseModel):
    id: UUID4
    name: str
    email: EmailStr
    is_approved: bool
    is_email_verified: bool
    
    class Config():
        from_attributes = True


class ListUsersResponse(BaseModel):
    status: str
    results: int
    users: List[ShowUsersResponse]

    class Config():
        from_attributes = True