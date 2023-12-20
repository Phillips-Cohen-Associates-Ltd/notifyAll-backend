from ..config.database import Base
from uuid import uuid4
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.sql import func

class Identification(Base):
        __tablename__ = 'identifications'
        id = Column(String(100), primary_key=True, default=str(uuid4()))
        name = Column(String(100), nullable=False)
        status = Column(Integer, default=1)
        created_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
        updated_at = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())


    