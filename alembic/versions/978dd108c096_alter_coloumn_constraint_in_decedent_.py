"""alter coloumn constraint in decedent requests

Revision ID: 978dd108c096
Revises: 8707aad0993e
Create Date: 2024-01-07 12:05:08.249561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String, Integer


# revision identifiers, used by Alembic.
revision: str = '978dd108c096'
down_revision: Union[str, None] = '8707aad0993e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
       op.alter_column('decedent_requests', Column('person_dealing_with_estate', Integer, nullable=False, server_default='1'))
       op.alter_column('decedent_requests', Column('identification_id', String(36), nullable=False, server_default='citizenship'))
       op.alter_column('decedent_requests', Column('is_verify_identity', String(5), nullable=False, server_default='1'))
       op.alter_column('decedent_requests', Column('id_number', String(30), nullable=False, server_default="555-555-5555"))


def downgrade() -> None:
    pass
