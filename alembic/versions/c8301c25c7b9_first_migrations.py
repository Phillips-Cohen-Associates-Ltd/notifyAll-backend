"""first migrations

Revision ID: c8301c25c7b9
Revises: 
Create Date: 2023-10-09 10:45:56.635588

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


#revision identifiers, used by Alembic.
revision: str = 'c8301c25c7b9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass