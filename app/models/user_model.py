from ..config.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import TIMESTAMP, Column, String, Boolean
import uuid
from uuid import uuid4
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Users(Base):
    __tablename__ = 'users'
    id = Column(String(100), primary_key=True, default=str(uuid4()))
    name = Column(String(100), nullable=False)
    email = Column(String(350), unique=True, nullable=False)
    password = Column(String(300), nullable=True)
    is_approved = Column(Boolean, nullable=False, default=False)
    is_email_verified = Column(Boolean, nullable=False, default=False)
    verification_code = Column(String(6), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())