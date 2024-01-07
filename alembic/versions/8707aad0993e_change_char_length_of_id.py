"""change char length of id

Revision ID: 8707aad0993e
Revises: 3e1581bfe970
Create Date: 2024-01-05 18:53:20.635462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8707aad0993e'
down_revision: Union[str, None] = '3e1581bfe970'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.alter_column('decedent_requests', 'id',
    #               existing_type=sa.VARCHAR(length=36),
    #               type_=sa.String(length=100),
    #               existing_nullable=False)
    op.alter_column('users', 'id',
                  existing_type=sa.VARCHAR(length=36),
                  type_=sa.String(length=100),
                  existing_nullable=False)
    # op.alter_column('decedent_requests_document', 'id',
    #               existing_type=sa.VARCHAR(length=36),
    #               type_=sa.String(length=100),
    #               existing_nullable=False)
    op.alter_column('relationships', 'id',
                  existing_type=sa.VARCHAR(length=36),
                  type_=sa.String(length=100),
                  existing_nullable=False)
    op.alter_column('identifications', 'id',
                  existing_type=sa.VARCHAR(length=36),
                  type_=sa.String(length=100),
                  existing_nullable=False)
    


def downgrade() -> None:
    pass
