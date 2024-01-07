"""alter table

Revision ID: 7a1fc1efa2d3
Revises: 978dd108c096
Create Date: 2024-01-07 12:20:56.047747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String

# revision identifiers, used by Alembic.
revision: str = '7a1fc1efa2d3'
down_revision: Union[str, None] = '978dd108c096'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.alter_column('decedent_requests', Column('person_dealing_with_estate', Integer, nullable=False, server_default='1'))
     op.alter_column('decedent_requests', Column('identification_id', String(36), nullable=False, server_default='citizenship'))
     op.alter_column('decedent_requests', Column('is_verify_identity', String(5), nullable=False, server_default='1'))
     op.alter_column('decedent_requests', Column('id_number', String(30), nullable=False, server_default="555-555-5555"))



def downgrade() -> None:
    pass
