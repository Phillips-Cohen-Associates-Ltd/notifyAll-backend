"""remove email_verified_table

Revision ID: 3ade53001a0c
Revises: b9a795a0a000
Create Date: 2023-12-12 12:03:40.436631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ade53001a0c'
down_revision: Union[str, None] = 'b9a795a0a000'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
  op.drop_column('users', 'is_email_verified')

def downgrade():
  op.add_column('users', sa.Column('is_email_verified', sa.Boolean(), nullable=True))
