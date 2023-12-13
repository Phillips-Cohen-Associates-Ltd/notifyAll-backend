from sqlalchemy import Column, String, String, Date, TIMESTAMP, BIGINT
from sqlalchemy.dialects.mysql import TINYINT
from ..config.database import Base

class CreditorPropertyUtilityDetailsDraft(Base):
    __tablename__ = "creditor_property_utility_details_draft"

    id = Column(String(36), primary_key=True)
    request_id = Column(String(36), nullable=False)
    creditor_id = Column(String(36), nullable=False)
    asset_type = Column(String(36), nullable=False)
    meter_read = Column(String(255), nullable=True)
    meter_read_date = Column(Date, nullable=True)
    is_approved = Column(TINYINT, nullable=False, default=0)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
    data_id = Column(String(255), nullable=True)
    dual_flag_code = Column(BIGINT, nullable=False, default=0, comment="1. Gas, 2. Electric")