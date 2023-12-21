"""add cities table

Revision ID: a72da024326f
Revises: ecbe4618e65e
Create Date: 2023-12-21 15:11:32.700544

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'a72da024326f'
down_revision: Union[str, None] = 'ecbe4618e65e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
