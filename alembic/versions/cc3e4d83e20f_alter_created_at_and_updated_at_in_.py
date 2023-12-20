"""alter created_at and updated_at in decedent requests

Revision ID: cc3e4d83e20f
Revises: f5fea8a6978d
Create Date: 2023-12-19 12:43:51.419006

"""
from typing import Sequence, Union
from sqlalchemy.sql import func
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = 'cc3e4d83e20f'
down_revision: Union[str, None] = 'f5fea8a6978d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.alter_column('decedent_requests', 'created_at', 
    #               existing_type=sa.TIMESTAMP(timezone=True), 
    #               nullable=False, 
    #               server_default=func.now())
    op.alter_column('decedent_requests', 'updated_at', 
                 existing_type=sa.TIMESTAMP(timezone=True), 
                   nullable=True, 
                   server_default=None, 
                   onupdate=func.now())
    op.execute(text("UPDATE decedent_requests SET created_at = NOW() WHERE created_at IS NULL"))



def downgrade() -> None:
    pass
