"""change data type length for dial code for country table

Revision ID: a08bca1fc585
Revises: 
Create Date: 2024-01-08 14:53:40.632749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a08bca1fc585'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('country', 'dial_code', type_=sa.String(length=100))



def downgrade() -> None:
    op.alter_column('country', 'dial_code', type_=sa.String(length=100))

