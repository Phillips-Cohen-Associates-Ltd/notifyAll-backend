from ..config.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Users(Base):
    __tablename__ = 'users'
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String(100), nullable=False)
    email = Column(String(350), unique=True, nullable=False)
    password = Column(String(300), nullable=True)
    is_approved = Column(Boolean, nullable=False, default=False)
<<<<<<< HEAD
    is_email_verified = Column(Boolean, nullable=False, default=False)
    verification_code = Column(String(6), nullable=True)
=======
>>>>>>> 8ddb522b8117e4a3318c8dd16e6d87511e845659
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())
