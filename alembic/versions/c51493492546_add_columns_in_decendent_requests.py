"""add columns in decendent Requests

Revision ID: c51493492546
Revises: ae708993e34f
Create Date: 2023-12-15 15:48:45.545029

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import String, Column, Integer


# revision identifiers, used by Alembic.
revision: str = 'c51493492546'
down_revision: Union[str, None] = 'ae708993e34f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   pass

def downgrade():
   pass


