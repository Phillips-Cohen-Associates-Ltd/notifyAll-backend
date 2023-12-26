"""add foriegn keys

Revision ID: 1dbb015dcdf7
Revises: a72da024326f
Create Date: 2023-12-21 16:51:47.198084

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1dbb015dcdf7'
down_revision: Union[str, None] = 'a72da024326f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('state', sa.Column('country_id', sa.Integer, sa.ForeignKey('country.id')))
    op.add_column('city', sa.Column('state_id', sa.Integer, sa.ForeignKey('state.id')))




def downgrade() -> None:
    pass
