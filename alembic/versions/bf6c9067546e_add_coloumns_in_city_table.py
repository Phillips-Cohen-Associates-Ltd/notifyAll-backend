"""add coloumns in city table

Revision ID: bf6c9067546e
Revises: 7a1fc1efa2d3
Create Date: 2024-01-07 17:23:53.009177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf6c9067546e'
down_revision: Union[str, None] = '7a1fc1efa2d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.add_column('country', sa.Column('iso2', sa.String(length=5)))
   op.add_column('country', sa.Column('dial_code', sa.String(100)))
   op.add_column('city', sa.Column('country_id', sa.Integer(), sa.ForeignKey('country.id')))


def downgrade() -> None:
    pass
