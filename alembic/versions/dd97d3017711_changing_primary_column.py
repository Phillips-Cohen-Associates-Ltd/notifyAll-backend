"""changing primary column

Revision ID: dd97d3017711
Revises: 30e7b1d6114b
Create Date: 2023-12-13 15:47:58.466657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd97d3017711'
down_revision: Union[str, None] = '30e7b1d6114b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     # Drop the existing primary key constraint
   op.drop_constraint('PRIMARY', 'states', type_='primary')

   # Change the type of the column
   op.alter_column('states', 'name', existing_type=sa.String(100), type_=sa.VARCHAR(length=255))

   # Create a new primary key constraint
   op.create_primary_key('states_pkey', 'states', ['name'])


def downgrade() -> None:
    pass




