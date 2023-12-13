"""changing primary column of cities table

Revision ID: 55786cd0895a
Revises: dd97d3017711
Create Date: 2023-12-13 16:35:33.845433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55786cd0895a'
down_revision: Union[str, None] = 'dd97d3017711'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
       op.create_primary_key('cities_pkey', 'cities', ['name'])

def downgrade() -> None:
    pass
