from sqlalchemy import Column, String, String, TIMESTAMP, PrimaryKeyConstraint, Integer
from ..config.database import Base


class DecedentRequestDocument(Base):
    __tablename__ = "decedent_request_document"

    id = Column(String(36), primary_key=True)
    request_id = Column(String(36), nullable=False)
    document = Column(String(255), nullable=False)
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
    size = Column(String(255), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint(id, request_id),
    )