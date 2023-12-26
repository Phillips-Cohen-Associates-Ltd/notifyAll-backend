"""change constraint of city_state column

Revision ID: ecbe4618e65e
Revises: f8dabdc58092
Create Date: 2023-12-21 15:04:20.607365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecbe4618e65e'
down_revision: Union[str, None] = 'f8dabdc58092'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('existing_pkey', 'state', type_='primary')
    op.create_primary_key('new_pkey', 'state', ['id'])



def downgrade() -> None:
    pass
