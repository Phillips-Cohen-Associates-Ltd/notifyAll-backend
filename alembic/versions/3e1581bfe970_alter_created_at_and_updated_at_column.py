"""alter created at and updated at column

Revision ID: 3e1581bfe970
Revises: eab4e33bef27
Create Date: 2023-12-27 15:39:08.565969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e1581bfe970'
down_revision: Union[str, None] = 'eab4e33bef27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.alter_column('decedent_request_document', sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()))
   op.alter_column('decedent_request_document', sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now()))


def downgrade() -> None:
    pass
